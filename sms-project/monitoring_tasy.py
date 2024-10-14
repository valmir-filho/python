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
        # Structure of the data payload to be sent via the API.
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
            # Sending a POST request to the API with the SMS data and authentication.
            response = requests.post(api_url, json=sms_data, auth=HTTPBasicAuth(api_username, api_password), timeout=10)
            # Check if the SMS was successfully sent (HTTP status 200).
            if response.status_code == 200:
                print(f"SMS enviado com sucesso para o celular: {cellphone}.")
            else:
                print(f"Falha ao enviar o SMS: {response.status_code}\nDetalhes: {response.text}.")
        except requests.exceptions.RequestException as e:
            # Handles any exceptions related to the request (e.g., timeouts, connection errors).
            print(f"Erro ao enviar o SMS para o celular {cellphone}: {e}.")


# Function to check the status of containers in the database.
def check_container_status():
    # Creates the Data Source Name (DSN) for the Oracle connection.
    dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)
    try:
        # Establishes a connection to the Oracle database.
        connection = cx_Oracle.connect(user=db_username, password=db_password, dsn=dsn_tns)
        cursor = connection.cursor()
        # SQL query to retrieve the tag_name and port_jmx from the app_container table.
        query = """
        SELECT tag_name, port_jmx 
        FROM app_container
        WHERE tag_name IN ('tasy/tasyreports', 'tasy/tasyemr', 'tasy/tasyjava', 'tasy/tasyappserver', 'tasy/tasyschedulerweb')
        """
        cursor.execute(query)  # Executes the SQL query.
        results = cursor.fetchall()  # Fetches all the results.
        # Verifies if the number of returned rows is 7 (since we expect 7 containers in production).
        if len(results) != 7:
            # Sends an SMS alert if the number of containers is not what is expected.
            send_sms_alert("Alerta! Um dos containers do PAM do Tasy foi removido. Verifique em: https://172.19.219.58:8443/#!/login",
                           ["41999999999", "41999999999"])
        # Loops through each result (each container) and checks if its port_jmx is 0.
        for tag_name, port_jmx in results:
            if port_jmx == 0:
                # If port_jmx is 0, sends an SMS alert about the specific container that has an issue.
                message = f"Alerta! O container {tag_name} do PAM Tasy está com problema. Verifique em: https://172.19.219.58:8443/#!/login"
                send_sms_alert(message, ["41999999999", "41999999999"])
        cursor.close()  # Closes the cursor.
        connection.close()  # Closes the database connection.
    except cx_Oracle.DatabaseError as e:
        # Handles any exceptions related to the database connection or query execution.
        print(f"Error accessing the database: {e}.")
        # Send an SMS alert regarding the database access issue.
        send_sms_alert("Alerta! O Banco de Dados do Tasy está com problema.",
                       ["41999999999", "41999999999"])


# Main function to check the overall system status.
def check_system_status():
    print("Checking the system status...")
    check_container_status()  # Calls the function to check container statuses.

# Infinite loop to check the system status every 3 minutes.
while True:
    check_system_status()  # Executes the system status check.
    time.sleep(180)  # Waits for 180 seconds (3 minutes) before repeating the check.
