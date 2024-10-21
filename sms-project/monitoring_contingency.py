# Imports required libraries.
import cx_Oracle
import requests
import time
from requests.auth import HTTPBasicAuth

# Database connection details for the production environment.
host = ''
port = ''
service_name = ''
db_username = ''
db_password = ''

# API endpoint URL for sending SMS.
api_url = 'https://api360.classeaservicos.com.br/api/send.php'

# API authentication credentials (username and password).
api_username = ''
api_password = ''


# Function to send SMS alerts to a list of phone numbers.
def send_sms_alert(message, cellphones):
    for cellphone in cellphones:
        sms_data = {
            "codigo_carteira": "",
            "codigo_fornecedor": "",
            "envios": [
                {
                    "numero": cellphone,
                    "mensagem": message
                }
            ]
        }
        try:
            response = requests.post(api_url, json=sms_data, auth=HTTPBasicAuth(api_username, api_password), timeout=10)
            if response.status_code == 200:
                print(f"SMS enviado com sucesso para o celular: {cellphone}.")
            else:
                print(f"Falha ao enviar o SMS: {response.status_code}\nDetalhes: {response.text}.")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar o SMS para o celular {cellphone}: {e}.")


# Function to check the contingency status.
def check_contingency_status():
    # Creates the Data Source Name (DSN) for the Oracle connection.
    dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)
    try:
        # Establishes a connection to the Oracle database.
        connection = cx_Oracle.connect(user=db_username, password=db_password, dsn=dsn_tns)
        cursor = connection.cursor()
        # SQL query to check the last execution of the contingency process.
        query = """
        SELECT to_char(dt_ultima_execucao, 'dd/mm/yyyy hh24:mi')
        FROM FEAES_TASYGER_LAST_EXEC
        WHERE dt_ultima_execucao <= sysdate - 2/24
        """
        cursor.execute(query)  # Executes the SQL query.
        result = cursor.fetchone()  # Fetches the first result (if any).
        
        if result:  # If there is a result, it means there's an issue with the contingency update.
            dt_ultima_execucao = result[0]  # Retrieves the date and time from the query result.
            # Construct the message with the formatted date and time.
            message = (
                f"A contingência está sem atualização desde {dt_ultima_execucao}. "
                "Verifique a execução do TasySchedulerWeb acessando o link: "
                "https://tasy-feas.curitiba.pr.gov.br/TasySchedulerWeb/#/jobs com usuário: whebservidor "
                "e senha disponível na FAQ do CPD."
            )
            # Sends the constructed message via SMS.
            send_sms_alert(message, ["", "", "", ""])
        
        cursor.close()  # Closes the cursor.
        connection.close()  # Closes the database connection.
    except cx_Oracle.DatabaseError as e:
        print(f"Error accessing the database: {e}.")
        send_sms_alert("Alerta! Erro ao acessar o banco de dados para verificar a contingência.",
                       ["", "", "", ""])


# Main function to check the system status.
def check_system_status():
    print("Checking the contingency status...")
    check_contingency_status()  # Check the contingency update status.

# Infinite loop to check the system status every 3 minutes.
while True:
    check_system_status()  # Executes the system status check.
    time.sleep(180)  # Waits for 180 seconds (3 minutes) before repeating the check.
