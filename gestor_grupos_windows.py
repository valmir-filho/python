from __future__ import annotations

import hmac
import logging
import os
import re
import secrets
import subprocess
import sys
import time
from pathlib import Path
from typing import Final

from flask import Flask, render_template_string, request, jsonify, redirect, url_for, session, abort
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)


# =============================================================================
# CONFIGURAÇÕES
# =============================================================================

# Usuário administrador da aplicação.
# Pode ser alterado via variável de ambiente APP_ADMIN_USER.
USER_ADMIN: Final[str] = os.environ.get("APP_ADMIN_USER", "adminexe")

# Senha do administrador.
# Obrigatório definir via variável de ambiente APP_ADMIN_PASSWORD.
# Exemplo no Windows PowerShell: setx APP_ADMIN_PASSWORD "sua_senha_forte"
PASSWORD_ADMIN: Final[str | None] = os.environ.get("APP_ADMIN_PASSWORD")

# Chave secreta do Flask.
# Obrigatória definir via variável de ambiente FLASK_SECRET_KEY.
# Exemplo para gerar uma chave: python -c "import secrets; print(secrets.token_hex(32))"
FLASK_SECRET_KEY: Final[str | None] = os.environ.get("FLASK_SECRET_KEY")

# Quando estiver atrás de HTTPS, defina APP_COOKIE_SECURE=1.
COOKIE_SECURE: Final[bool] = os.environ.get("APP_COOKIE_SECURE", "0") == "1"

# Porta da aplicação.
APP_PORT: Final[int] = int(os.environ.get("APP_PORT", "5000"))

# Arquivo de log.
LOG_FILE: Final[Path] = Path(os.environ.get("APP_LOG_FILE", "appPS_auditoria.log"))

# Quantidade máxima de tentativas inválidas de login por IP dentro da janela.
MAX_LOGIN_ATTEMPTS: Final[int] = 5

# Janela de bloqueio em segundos.
LOGIN_BLOCK_SECONDS: Final[int] = 10 * 60

# Caracteres permitidos para grupo/usuário.
# Como o subprocess é executado sem shell=True, o risco de injeção diminui bastante, mas ainda validamos para evitar entradas estranhas e erros operacionais.
SAFE_NAME_REGEX: Final[re.Pattern[str]] = re.compile(r"^[\wÀ-ÿ .@\\/\-$]+$", re.UNICODE)


# =============================================================================
# VALIDAÇÃO DE AMBIENTE
# =============================================================================

if not PASSWORD_ADMIN:
    raise RuntimeError(
        "A variável de ambiente APP_ADMIN_PASSWORD não foi definida. "
        "Defina uma senha forte antes de iniciar a aplicação."
    )

if not FLASK_SECRET_KEY:
    raise RuntimeError(
        "A variável de ambiente FLASK_SECRET_KEY não foi definida. "
        "Gere uma chave forte com: python -c \"import secrets; print(secrets.token_hex(32))\""
    )

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


# =============================================================================
# LOGS
# =============================================================================

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


# =============================================================================
# APLICAÇÃO FLASK
# =============================================================================

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=COOKIE_SECURE,
)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "Faça login para acessar o sistema."


class Usuario(UserMixin):
    """Representa o usuário autenticado no Flask-Login."""

    def __init__(self, user_id: str):
        self.id = user_id


@login_manager.user_loader
def load_user(user_id: str) -> Usuario | None:
    """Carrega o usuário salvo na sessão."""
    if user_id == USER_ADMIN:
        return Usuario(user_id)
    return None


# Controle simples em memória para tentativas de login.
# Em produção com múltiplos processos/servidores, use Redis ou banco.
LOGIN_ATTEMPTS: dict[str, list[float]] = {}


# =============================================================================
# FUNÇÕES AUXILIARES DE SEGURANÇA
# =============================================================================

def get_client_ip() -> str:
    """Obtém o IP de origem da requisição."""
    return request.headers.get("X-Forwarded-For", request.remote_addr or "desconhecido").split(",")[0].strip()


def is_login_blocked(ip: str) -> bool:
    """Verifica se o IP está temporariamente bloqueado por falhas de login."""
    now = time.time()
    attempts = LOGIN_ATTEMPTS.get(ip, [])

    # Mantém somente tentativas dentro da janela de bloqueio.
    attempts = [t for t in attempts if now - t <= LOGIN_BLOCK_SECONDS]
    LOGIN_ATTEMPTS[ip] = attempts

    return len(attempts) >= MAX_LOGIN_ATTEMPTS


def register_failed_login(ip: str) -> None:
    """Registra uma tentativa inválida de login."""
    LOGIN_ATTEMPTS.setdefault(ip, []).append(time.time())


def clear_failed_logins(ip: str) -> None:
    """Limpa falhas após login correto."""
    LOGIN_ATTEMPTS.pop(ip, None)


def generate_csrf_token() -> str:
    """Gera e salva token CSRF na sessão."""
    token = secrets.token_urlsafe(32)
    session["csrf_token"] = token
    return token


def validate_csrf_token(token: str | None) -> bool:
    """Valida token CSRF recebido pelo formulário ou API."""
    saved_token = session.get("csrf_token")
    return bool(saved_token and token and hmac.compare_digest(saved_token, token))


def validar_nome(valor: str, campo: str) -> str:
    """
    Valida nomes recebidos do navegador.

    Aceita letras, números, acentos, espaço, ponto, underline, hífen,
    barra, contrabarra, arroba e cifrão.
    """
    valor = (valor or "").strip()

    if not valor:
        raise ValueError(f"{campo} não pode estar vazio.")

    if len(valor) > 128:
        raise ValueError(f"{campo} muito longo.")

    if not SAFE_NAME_REGEX.fullmatch(valor):
        raise ValueError(f"{campo} contém caracteres não permitidos.")

    return valor


def validar_grupo_existente(grupo: str) -> str:
    """Garante que o grupo informado existe na máquina antes de usá-lo."""
    grupo = validar_nome(grupo, "Grupo")
    grupos = listar_grupos()

    if grupo not in grupos:
        raise ValueError("Grupo inexistente ou não permitido.")

    return grupo


# =============================================================================
# EXECUÇÃO DE COMANDOS DO WINDOWS
# =============================================================================

def rodar_comando(args: list[str]) -> subprocess.CompletedProcess[str]:
    """
    Executa comando local sem shell=True.

    Isso evita que caracteres especiais sejam interpretados pelo shell/cmd.
    """
    try:
        resultado = subprocess.run(
            args,
            shell=False,
            capture_output=True,
            text=True,
            encoding="cp850",
            errors="replace",
            timeout=15,
            check=False,
        )
        return resultado

    except subprocess.TimeoutExpired as exc:
        logger.exception("Timeout ao executar comando: %s", args)
        raise RuntimeError("Tempo limite excedido ao executar comando.") from exc

    except OSError as exc:
        logger.exception("Erro operacional ao executar comando: %s", args)
        raise RuntimeError("Falha ao executar comando no sistema operacional.") from exc


def listar_grupos() -> list[str]:
    """Lista os grupos locais da máquina Windows."""
    resultado = rodar_comando(["net", "localgroup"])

    if resultado.returncode != 0:
        logger.error("Erro ao listar grupos: %s", resultado.stderr)
        raise RuntimeError("Não foi possível listar os grupos locais.")

    grupos = [
        linha.strip("* ").strip()
        for linha in resultado.stdout.splitlines()
        if linha.strip().startswith("*")
    ]

    return sorted(grupos)


def listar_membros(grupo: str) -> list[str]:
    """Lista os membros de um grupo local."""
    grupo = validar_grupo_existente(grupo)
    resultado = rodar_comando(["net", "localgroup", grupo])

    if resultado.returncode != 0:
        logger.error("Erro ao listar membros do grupo %s: %s", grupo, resultado.stderr)
        raise RuntimeError("Não foi possível listar os membros do grupo.")

    membros: list[str] = []
    coletando = False

    for linha in resultado.stdout.splitlines():
        texto = linha.strip()

        if "---" in texto:
            coletando = True
            continue

        if not coletando:
            continue

        if "concluído" in texto.lower() or "completed" in texto.lower():
            break

        if texto:
            # Preserva o nome original, mas remove excesso de espaços.
            membros.append(texto)

    return membros


def alterar_membro_grupo(grupo: str, usuario: str, operacao: str) -> None:
    """Adiciona ou remove um usuário de um grupo local."""
    grupo = validar_grupo_existente(grupo)
    usuario = validar_nome(usuario, "Usuário")

    if operacao == "/delete":
        args = ["net", "localgroup", grupo, usuario, "/delete"]
        acao = "REMOVEU"
    elif operacao == "/add":
        args = ["net", "localgroup", grupo, usuario, "/add"]
        acao = "ADICIONOU"
    else:
        raise ValueError("Operação inválida.")

    resultado = rodar_comando(args)

    ip = get_client_ip()
    operador = current_user.get_id() if current_user.is_authenticated else "desconhecido"

    if resultado.returncode != 0:
        logger.warning(
            "FALHA | operador=%s | ip=%s | acao=%s | grupo=%s | usuario=%s | erro=%s",
            operador,
            ip,
            acao,
            grupo,
            usuario,
            resultado.stderr.strip() or resultado.stdout.strip(),
        )
        raise RuntimeError(resultado.stderr.strip() or resultado.stdout.strip() or "Falha ao alterar grupo.")

    logger.info(
        "SUCESSO | operador=%s | ip=%s | acao=%s | grupo=%s | usuario=%s",
        operador,
        ip,
        acao,
        grupo,
        usuario,
    )


# =============================================================================
# TEMPLATES HTML
# =============================================================================

LOGIN_TEMPLATE = r"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Login - Gestor de Grupos</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >

    <style>
        body {
            background-color: #f0f2f5;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            font-family: sans-serif;
        }

        .card-login {
            width: 400px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
    </style>
</head>

<body>
    <div class="card card-login p-4 bg-white">
        <h3 class="text-center text-primary mb-4">🔐 Acesso ao Servidor</h3>

        {% if erro %}
            <div class="alert alert-danger p-2 text-center" style="font-size: 14px;">
                {{ erro }}
            </div>
        {% endif %}

        <form method="POST" autocomplete="off">
            <input type="hidden" name="csrf_token" value="{{ csrf_token }}">

            <div class="mb-3">
                <label class="form-label">Usuário</label>
                <input type="text" name="username" class="form-control" required autofocus>
            </div>

            <div class="mb-3">
                <label class="form-label">Senha</label>
                <input type="password" name="password" class="form-control" required>
            </div>

            <button type="submit" class="btn btn-primary w-100">
                Entrar
            </button>
        </form>
    </div>
</body>
</html>
"""


PAINEL_TEMPLATE = r"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Gestor de Grupos Locais</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >

    <style>
        body {
            background-color: #f0f2f5;
            font-family: sans-serif;
            padding: 20px;
        }

        .card-custom {
            height: 550px;
            overflow-y: auto;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .group-item {
            cursor: pointer;
            transition: 0.2s;
        }

        .group-item:hover {
            background-color: #f8f9fa;
        }

        .active-group {
            background-color: #0d6efd !important;
            color: white !important;
        }

        .small-muted {
            font-size: 12px;
            color: #6c757d;
        }
    </style>
</head>

<body>
    <div class="container">

        <div class="d-flex justify-content-between align-items-center mb-4">
            <div>
                <h2 class="text-primary m-0">🖥️ Gestor de Grupos e Usuários</h2>
                <div class="small-muted">Usuário logado: {{ usuario_logado }}</div>
            </div>

            <a href="/logout" class="btn btn-outline-danger btn-sm">
                Sair
            </a>
        </div>

        <div id="alerta" class="alert d-none" role="alert"></div>

        <div class="row">

            <div class="col-md-4">
                <div class="card card-custom">
                    <div class="card-header bg-white">
                        <b>Grupos</b>
                    </div>

                    <div class="list-group list-group-flush">
                        {% for g in grupos %}
                            <button
                                type="button"
                                class="list-group-item list-group-item-action group-item"
                                data-grupo="{{ g }}"
                                onclick="carregarMembros(this.dataset.grupo, this)"
                            >
                                {{ g }}
                            </button>
                        {% endfor %}
                    </div>
                </div>
            </div>

            <div class="col-md-5">
                <div class="card card-custom">
                    <div class="card-header bg-white d-flex justify-content-between">
                        <b>Membros</b>
                        <span id="nomeGrupo" class="badge bg-secondary">-</span>
                    </div>

                    <div id="listaMembros" class="list-group list-group-flush">
                        <div class="p-4 text-center text-muted">
                            Selecione um grupo
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-md-3">
                <div class="card p-3 shadow-sm">
                    <h6>Adicionar Usuário</h6>

                    <input
                        type="text"
                        id="userIn"
                        class="form-control mb-2"
                        placeholder="usuario ou DOMINIO\usuario"
                        maxlength="128"
                    >

                    <button class="btn btn-primary w-100" onclick="acao('/add')">
                        Adicionar
                    </button>
                </div>
            </div>

        </div>
    </div>

    <script>
        let selecionado = "";
        const csrfToken = "{{ csrf_token }}";

        function mostrarAlerta(tipo, mensagem) {
            const alerta = document.getElementById("alerta");
            alerta.className = `alert alert-${tipo}`;
            alerta.innerText = mensagem;
            alerta.classList.remove("d-none");

            setTimeout(() => {
                alerta.classList.add("d-none");
            }, 5000);
        }

        function escapeHtml(valor) {
            return String(valor)
                .replaceAll("&", "&amp;")
                .replaceAll("<", "&lt;")
                .replaceAll(">", "&gt;")
                .replaceAll('"', "&quot;")
                .replaceAll("'", "&#039;");
        }

        function carregarMembros(g, el) {
            selecionado = g;

            document.getElementById("nomeGrupo").innerText = g;

            document.querySelectorAll(".group-item")
                .forEach(i => i.classList.remove("active-group"));

            el.classList.add("active-group");

            fetch("/api/membros/" + encodeURIComponent(g))
                .then(async response => {
                    const data = await response.json();

                    if (!response.ok) {
                        throw new Error(data.error || "Erro ao carregar membros.");
                    }

                    return data;
                })
                .then(data => {
                    const html = data.membros.map(m => {
                        const seguro = escapeHtml(m);

                        return `
                            <div class="list-group-item d-flex justify-content-between align-items-center">
                                <span>${seguro}</span>
                                <button
                                    class="btn btn-sm btn-danger"
                                    data-usuario="${seguro}"
                                    onclick="acao('/delete', this.dataset.usuario)"
                                >
                                    Remover
                                </button>
                            </div>
                        `;
                    }).join("");

                    document.getElementById("listaMembros").innerHTML =
                        html || '<div class="p-3 text-muted">Vazio</div>';
                })
                .catch(error => {
                    mostrarAlerta("danger", error.message);
                });
        }

        function acao(op, user = null) {
            const campoUsuario = document.getElementById("userIn");
            const usuario = (user || campoUsuario.value).trim();

            if (!selecionado) {
                mostrarAlerta("warning", "Selecione um grupo primeiro.");
                return;
            }

            if (!usuario) {
                mostrarAlerta("warning", "Informe um usuário.");
                return;
            }

            fetch("/api/acao", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRF-Token": csrfToken
                },
                body: JSON.stringify({
                    g: selecionado,
                    u: usuario,
                    op: op
                })
            })
            .then(async response => {
                const data = await response.json();

                if (!response.ok) {
                    throw new Error(data.error || "Erro ao executar ação.");
                }

                return data;
            })
            .then(data => {
                campoUsuario.value = "";
                mostrarAlerta("success", data.message || "Ação executada com sucesso.");

                const active = document.querySelector(".active-group");
                if (active) {
                    carregarMembros(selecionado, active);
                }
            })
            .catch(error => {
                mostrarAlerta("danger", error.message);
            });
        }
    </script>
</body>
</html>
"""


# =============================================================================
# ROTAS DE AUTENTICAÇÃO
# =============================================================================

@app.route("/login", methods=["GET", "POST"])
def login():
    """Tela de login."""
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    ip = get_client_ip()
    erro = None

    if is_login_blocked(ip):
        erro = "Muitas tentativas inválidas. Aguarde alguns minutos e tente novamente."
        csrf_token = generate_csrf_token()
        return render_template_string(LOGIN_TEMPLATE, erro=erro, csrf_token=csrf_token), 429

    if request.method == "POST":
        csrf_form = request.form.get("csrf_token")

        if not validate_csrf_token(csrf_form):
            abort(400, description="Token CSRF inválido.")

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        usuario_ok = hmac.compare_digest(username, USER_ADMIN)
        senha_ok = hmac.compare_digest(password, PASSWORD_ADMIN)

        if usuario_ok and senha_ok:
            clear_failed_logins(ip)
            login_user(Usuario(username))
            logger.info("LOGIN_SUCESSO | usuario=%s | ip=%s", username, ip)
            return redirect(url_for("index"))

        register_failed_login(ip)
        logger.warning("LOGIN_FALHA | usuario=%s | ip=%s", username, ip)
        erro = "Usuário ou senha incorretos."

    csrf_token = generate_csrf_token()
    return render_template_string(LOGIN_TEMPLATE, erro=erro, csrf_token=csrf_token)


@app.route("/logout")
@login_required
def logout():
    """Encerra a sessão do usuário."""
    usuario = current_user.get_id()
    ip = get_client_ip()

    logout_user()
    session.clear()

    logger.info("LOGOUT | usuario=%s | ip=%s", usuario, ip)
    return redirect(url_for("login"))


# =============================================================================
# ROTAS DA APLICAÇÃO
# =============================================================================

@app.route("/")
@login_required
def index():
    """Tela principal com a lista de grupos locais."""
    try:
        grupos = listar_grupos()
    except RuntimeError as exc:
        logger.exception("Erro ao abrir tela principal.")
        grupos = []
        # Em caso de erro, mostra a tela vazia e o usuário verá a lista sem grupos.
        # O erro fica registrado no log.

    csrf_token = generate_csrf_token()

    return render_template_string(
        PAINEL_TEMPLATE,
        grupos=grupos,
        usuario_logado=current_user.get_id(),
        csrf_token=csrf_token,
    )


@app.route("/api/membros/<path:g>")
@login_required
def api_membros(g: str):
    """API que retorna os membros de um grupo local."""
    try:
        membros = listar_membros(g)
        return jsonify({"membros": membros})

    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    except RuntimeError as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/acao", methods=["POST"])
@login_required
def api_acao():
    """API para adicionar ou remover usuário de grupo local."""
    csrf_header = request.headers.get("X-CSRF-Token")

    if not validate_csrf_token(csrf_header):
        return jsonify({"error": "Token CSRF inválido."}), 400

    dados = request.get_json(silent=True) or {}

    try:
        grupo = dados.get("g", "")
        usuario = dados.get("u", "")
        operacao = dados.get("op", "")

        alterar_membro_grupo(grupo, usuario, operacao)

        mensagem = "Usuário removido com sucesso." if operacao == "/delete" else "Usuário adicionado com sucesso."
        return jsonify({"success": True, "message": mensagem})

    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    except RuntimeError as exc:
        return jsonify({"error": str(exc)}), 500


# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

if __name__ == "__main__":
    # Para uso interno, o Flask pode escutar em 0.0.0.0.
    # Em produção, prefira rodar atrás de IIS/Nginx/Apache com HTTPS.
    app.run(host="0.0.0.0", port=APP_PORT, debug=False)
