# Importa bibliotecas para requisições HTTP e autenticação básica.
import requests
from requests.auth import HTTPBasicAuth
import time  # Para controle de intervalo de execução.

# Importa as classes da biblioteca jmxquery, usada para conexão JMX e consulta de métricas Java.
from jmxquery import JMXConnection, JMXQuery

# Tenta importar a exceção JMXQueryException para tratamento de erros da biblioteca jmxquery.
try:
    from jmxquery import JMXQueryException
except ImportError:
    import jpype
    JMXQueryException = jpype.JException  # Alternativa caso a exceção não exista diretamente.

# --- Configurações da API de SMS ---
api_url = 'https://api360.classeaservicos.com.br/api/send.php'  # Endpoint da API de envio de SMS.
api_username = 'ti@feas.curitiba.pr.gov.br'  # Usuário de autenticação.
api_password = 'rA8$T7kz#Qw3@Mn9'  # Senha de autenticação.

# --- Configurações de Alerta ---
alert_phones = ["41991256214", "41999580050", "41996166090", "41996907249"]  # Números que receberão os alertas.
CPU_THRESHOLD = 50.0  # Limite de uso de CPU (%) para disparar o alerta.

# --- Lista de Servidores JMX a Monitorar ---
jmx_targets = [
    {"host": "172.19.219.58", "port": 6002},  # Primeiro servidor com porta JMX.
    {"host": "172.19.219.58", "port": 6003}   # Segundo servidor com outra porta JMX.
]

# --- Função para Envio de SMS ---
def send_sms_alert(message, cellphones):
    # Envia a mensagem para cada número da lista.
    for cellphone in cellphones:
        sms_data = {
            "codigo_carteira": "124761724767135",  # Código da carteira (fixo pela API).
            "codigo_fornecedor": "classea_token",  # Identificador do fornecedor (fixo pela API).
            "envios": [
                {
                    "numero": cellphone,     # Número de celular destino.
                    "mensagem": message      # Mensagem de alerta.
                }
            ]
        }
        try:
            # Faz requisição POST para enviar o SMS.
            response = requests.post(api_url, json=sms_data, auth=HTTPBasicAuth(api_username, api_password), timeout=10)
            # Verifica se a resposta foi bem-sucedida.
            if response.status_code == 200:
                print(f"SMS enviado com sucesso para o celular: {cellphone}")
            else:
                print(f"Falha ao enviar SMS para o celular {cellphone}: {response.status_code} | {response.text}")
        except requests.exceptions.RequestException as e:
            # Captura erros de conexão, timeout, etc.
            print(f"Erro ao enviar o SMS para o celular {cellphone}: {e}")

# --- Função para Verificar CPU via JMX (usando jmxquery) ---
def check_cpu_for_host(jmx_host, jmx_port):
    # Monta a URL para conectar via protocolo RMI ao servidor JMX.
    jmx_url = f"service:jmx:rmi:///jndi/rmi://{jmx_host}:{jmx_port}/jmxrmi"
    jmx_conn = None 

    try:
        # Estabelece a conexão JMX.
        jmx_conn = JMXConnection(jmx_url)
        print(f"Conectado ao JMX em {jmx_host}:{jmx_port}")

        # Cria uma query para coletar o uso de CPU do processo Java.
        cpu_query_obj = JMXQuery("java.lang:type=OperatingSystem", "ProcessCpuLoad")
        query_result = jmx_conn.query([cpu_query_obj])  # Envia a consulta como uma lista.

        cpu_load = None
        if query_result and len(query_result) > 0:
            cpu_load = query_result[0].value  # Captura o valor da CPU retornado.
        else:
            print(f"Nenhum resultado para a query de CPU em {jmx_host}:{jmx_port}.")
            return

        # Verifica se o valor da CPU é válido
        if cpu_load is None or not isinstance(cpu_load, (int, float)) or cpu_load < 0:
            print(f"CPU inválida ou não encontrada para {jmx_host}:{jmx_port}")
            return

        # Converte o valor da CPU (0.0 a 1.0) para porcentagem.
        cpu_percent = cpu_load * 100
        print(f"CPU de {jmx_host}:{jmx_port} = {cpu_percent:.2f}%")

        # Se o uso da CPU estiver acima do limite definido, envia alerta por SMS.
        if cpu_percent > CPU_THRESHOLD:
            msg = (
                f"Aviso! Consumo da CPU do appserver ({jmx_host}:{jmx_port}) "
                f"acima de {cpu_percent:.2f}%. Avise um Analista."
            )
            send_sms_alert(msg, alert_phones)

    except JMXQueryException as e:
        # Erros específicos da biblioteca jmxquery.
        print(f"Erro de JMXQuery ao monitorar {jmx_host}:{jmx_port}: {e}")
        send_sms_alert(f"Erro JMXQuery ao monitorar CPU em {jmx_host}:{jmx_port}", alert_phones)
    except Exception as e:
        # Outros erros não tratados (por exemplo, rede, JMX fora do ar).
        print(f"Erro inesperado ao monitorar {jmx_host}:{jmx_port}: {e}")
        send_sms_alert(f"Erro inesperado ao monitorar CPU em {jmx_host}:{jmx_port}", alert_phones)
    finally:
        # A biblioteca jmxquery gerencia o fechamento automaticamente.
        print(f"Conexao JMX para {jmx_host}:{jmx_port} nao precisa ser explicitamente fechada.")

# --- Loop Principal de Monitoramento ---
while True:
    print("Iniciando monitoramento dos servidores JMX (via jmxquery)...")
    for target in jmx_targets:
        # Verifica a CPU de cada host configurado.
        check_cpu_for_host(target["host"], target["port"])
    time.sleep(180)  # Aguarda 3 minutos antes de repetir o monitoramento.
