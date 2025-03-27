# Importa bibliotecas necessárias para manipulação de arquivos, tempo e automação com Selenium.
import os
import shutil
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Define uma função que aguarda até o horário especificado antes de prosseguir com a execução.
def esperar_horario_alvo(hora_alvo="08:40"):
    agora = datetime.now()
    hoje_alvo = datetime.strptime(f"{agora.date()} {hora_alvo}", "%Y-%m-%d %H:%M")

    # Se o horário atual já passou do horário alvo, ajusta para o dia seguinte.
    if agora >= hoje_alvo:
        hoje_alvo += timedelta(days=1)

    # Calcula o tempo de espera em segundos e aguarda.
    tempo_espera = (hoje_alvo - agora).total_seconds()
    print(f"Aguardando até {hoje_alvo.strftime('%H:%M')} para iniciar... ({int(tempo_espera)} segundos)")
    time.sleep(tempo_espera)

# Chama a função para aguardar até o horário definido.
esperar_horario_alvo("08:40")

# Configura opções do navegador Edge para desativar detecção de automação e configurar proxy.
edge_options = Options()
edge_options.add_argument(f'--proxy-server={proxy_host}:{proxy_port}')
edge_options.add_argument("--disable-blink-features=AutomationControlled")
edge_options.add_experimental_option("useAutomationExtension", False)
edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Inicializa o driver do Edge com as opções definidas.
driver = webdriver.Edge(options=edge_options)
driver.get("http://esaude.curitiba.pr.gov.br/PortalSaude/portal.do?formAction=init&v=2")
driver.maximize_window()

try:
    # Aguarda o carregamento do frame principal da página e alterna para ele.
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "content"))
    )

    # Preenche o nome de usuário.
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "user.name"))
    )
    username.send_keys("eduardo.silva4")

    # Preenche a senha e envia o formulário.
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user.password"))
    )
    password.send_keys("87748557e")
    password.send_keys(Keys.RETURN)

    # Retorna ao conteúdo principal da página.
    driver.switch_to.default_content()

    # Aguarda novamente o carregamento do frame de conteúdo.
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "content"))
    )

    # Fecha a janela de aviso, se existir.
    try:
        aviso = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "btPopupCancelmensagemSistema"))
        )
        aviso.click()
        print("Tela de aviso fechada com sucesso.")
    except:
        print("Nenhuma tela de aviso encontrada.")

    # Clica no ícone do menu.
    try:
        icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "icone_33"))
        )
        icon.click()
        print("Ícone clicado com sucesso.")
    except:
        print("Ícone não encontrado ou não clicável.")
        driver.quit()

    # Aguarda o carregamento e troca de janela.
    time.sleep(2)
    main_window = driver.current_window_handle
    all_windows = driver.window_handles
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)
            break

    print("Mudança para a nova janela concluída com sucesso.")
    time.sleep(2)

    # Move o mouse até o menu "Relatórios Dinâmicos".
    menu_relatorios_dinamicos = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mnuRelatoriosDinamicos.menuItem"))
    )
    action = ActionChains(driver)
    action.move_to_element(menu_relatorios_dinamicos).perform()
    print("Mouse movido para o menu 'Relatórios Dinâmicos'.")

    time.sleep(1)

    # Clica na opção "Relatórios Administrativos UPA".
    menu_relatorios_adm_upa = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mnuRelatoriosAdmUPA.menuItem"))
    )
    menu_relatorios_adm_upa.click()
    print("Clique no item 'Relatórios Administrativos UPA' realizado com sucesso.")

    time.sleep(3)

    # Navega para os iframes necessários.
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "content"))
    )
    print("Mudança para o iframe 'content' realizada com sucesso.")

    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "rText"))
    )
    print("Mudança para o iframe 'rText' realizada com sucesso.")

    # Clica no botão para abrir o popup de filtros.
    botao_abrir_popup = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "formulario:tabs:tabela:0:j_idt54"))
    )
    botao_abrir_popup.click()
    print("Botão do popup clicado com sucesso.")

    # Retorna ao conteúdo principal e muda para a nova janela do popup.
    driver.switch_to.default_content()
    time.sleep(2)
    all_windows = driver.window_handles
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)
            print("Mudança para a janela do popup realizada com sucesso.")
            break

    # Acessa os iframes do popup.
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "content"))
    )
    print("Mudança para o iframe 'content' do popup realizada com sucesso.")

    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "rText"))
    )
    print("Mudança para o iframe 'rText' do popup realizada com sucesso.")

    # Preenche os campos de data com a data do dia anterior.
    data_anterior = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y")

    campo_data1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "filtros:formParametros:tabelaParametros:0:j_idt155_input"))
    )
    campo_data1.click()
    campo_data1.send_keys(Keys.CONTROL + "a")
    campo_data1.send_keys(Keys.DELETE)
    campo_data1.send_keys(data_anterior)
    campo_data1.send_keys(Keys.TAB)
    print(f"Data Inicial preenchida corretamente com {data_anterior}.")

    campo_data2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "filtros:formParametros:tabelaParametros:1:j_idt155_input"))
    )
    campo_data2.click()
    campo_data2.send_keys(Keys.CONTROL + "a")
    campo_data2.send_keys(Keys.DELETE)
    campo_data2.send_keys(data_anterior)
    campo_data2.send_keys(Keys.TAB)
    print(f"Data Final preenchida corretamente com {data_anterior}.")

    # Fecha o calendário clicando fora, se possível.
    try:
        titulo_formulario = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "formulario"))
        )
        titulo_formulario.click()
        print("Calendário fechado clicando no formulário.")
    except:
        print("Não foi possível clicar no formulário para fechar o calendário.")

    # Seleciona a unidade UPA BOA VISTA no menu suspenso.
    menu_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "filtros:formParametros:tabelaParametros:2:j_idt143"))
    )
    menu_dropdown.click()
    print("Menu suspenso aberto.")

    upa_bv = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "filtros:formParametros:tabelaParametros:2:j_idt143_2"))
    )
    upa_bv.click()
    print("Opção 'UPA BOA VISTA' selecionada com sucesso.")

    # Confirma os filtros e realiza o download do relatório.
    botao_confirmar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "filtros:j_idt163:j_idt168"))
    )
    botao_confirmar.click()
    print("Botão 'Confirmar' clicado com sucesso.")

    botao_download = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "formDownload:downloadLink"))
    )
    botao_download.click()
    print("Botão 'Download' clicado com sucesso.")

    time.sleep(2)

finally:
    # Encerra o navegador após uma pausa.
    time.sleep(5)
    driver.quit()

# Define o caminho de origem onde o arquivo será baixado.
pasta_origem = r"C:\Users\vafilho\Downloads"

# Define a data de ontem para renomear o arquivo corretamente.
ontem = datetime.now() - timedelta(days=1)
data_formatada = ontem.strftime("%d-%m-%y")

# Mapeia os nomes dos arquivos para os novos nomes desejados.
renomeacoes = {
    "072_-_Atendimentos_nas_Unidade.xls": "072_UPABOAVISTA",
}

# Define os diretórios de destino para mover os arquivos.
pastas_destino = {
    "072": r"S:\_DAS\DAS_PBI\072 - ATENDIMENTO MÉDICO\2025"
}

# Move e renomeia os arquivos de acordo com os mapeamentos definidos.
for nome_antigo, base_nome_novo in renomeacoes.items():
    prefixo = base_nome_novo.split("_")[0]
    nome_novo = f"{base_nome_novo}_{data_formatada}.xls"

    caminho_antigo = os.path.join(pasta_origem, nome_antigo)
    pasta_destino = pastas_destino.get(prefixo)

    if pasta_destino:
        caminho_novo = os.path.join(pasta_destino, nome_novo)
        try:
            shutil.move(caminho_antigo, caminho_novo)
            print(f"Movido e renomeado: {nome_antigo} → {caminho_novo}.")
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {nome_antigo}.")
        except Exception as e:
            print(f"Erro ao mover/renomear {nome_antigo}: {e}.")
    else:
        print(f"Pasta de destino não definida para prefixo: {prefixo}.")
