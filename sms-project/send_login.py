# Imports.
import cx_Oracle
import re
import requests
import time
from requests.auth import HTTPBasicAuth

# DB production connection details.
host = ''
port = ''
service_name = ''
db_username = ''
db_password = ''

# API URL and authentication credentials.
api_url = 'https://api360.classeaservicos.com.br/api/send.php'
api_username = ''
api_password = ''


# Function to send SMS.
def send_sms(phone_number, login, password):
    sms_data = {
        "codigo_carteira": "",
        "codigo_fornecedor": "",
        "envios": [
            {
                "numero": phone_number,
                "mensagem": f"""Bem vindo(a) a FEAS! Para acessar o computador use:
Login: {login}
Senha: {password}"""
            }
        ]
    }

    try:
        response = requests.post(api_url, json=sms_data, auth=HTTPBasicAuth(api_username, api_password), timeout=10)

        if response.status_code == 200:
            print(f'Success: Password send to: {phone_number}.')
            return True
        else:
            print(f'Failed to send SMS: {response.status_code}\nDetails: {response.text}.')
            return False

    except requests.exceptions.RequestException as e:
        print(f'Error sending SMS: {e}.')
        return False


# Function to update order status in the database.
def update_order_status(nr_sequencia):
    dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)

    try:
        connection = cx_Oracle.connect(user=db_username, password=db_password, dsn=dsn_tns)
        cursor = connection.cursor()

        sql_update = """
        UPDATE MAN_ORDEM_SERVICO
        SET IE_STATUS_ORDEM = 3, NR_SEQ_ESTAGIO = 12, NM_USUARIO = 'vafilho', NM_USUARIO_EXEC = 'vafilho',
            DT_INICIO_REAL = SYSDATE, DT_FIM_REAL = SYSDATE
        WHERE NR_SEQUENCIA = :nr_sequencia
        """

        cursor.execute(sql_update, {'nr_sequencia': nr_sequencia})
        connection.commit()
        print(f'Success: Order status updated for sequence {nr_sequencia}.')

    except cx_Oracle.DatabaseError as e:
        print(f"Database error during update: {e}.")
    
    finally:
        cursor.close()
        connection.close()


# Function to process SQL results and send SMS.
def process_sql_results():
    dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)

    try:
        connection = cx_Oracle.connect(user=db_username, password=db_password, dsn=dsn_tns)
        cursor = connection.cursor()

        sql_query = """
        SELECT 
            mos.nr_sequencia,
            mos.ds_dano_breve,
            mos.ds_dano,
            most.ds_relat_tecnico
        FROM 
            man_ordem_servico mos
        JOIN 
            man_ordem_serv_tecnico most
        ON 
            mos.nr_sequencia = most.nr_seq_ordem_serv
        WHERE 
            mos.ds_dano_breve = 'Solicitação de login de usuário (automático)'
            AND mos.ie_status_ordem = 1
            AND mos.nr_seq_estagio = 21
        """

        cursor.execute(sql_query)
        result = cursor.fetchall()

        for row in result:
            nr_sequencia = row[0]
            ds_dano = row[2]
            ds_relat_tecnico = row[3]

            phone_match = re.search(r'Telefone:\s*(\d{2})\s*(\d{9})', ds_dano)
            if phone_match:
                phone_number = f'{phone_match.group(1)}{phone_match.group(2)}'
            else:
                phone_number = 'Phone not found.'

            login_match = re.search(r'login:\s*"([^"]+)"', ds_relat_tecnico)
            password_match = re.search(r'senha:\s*"([^"]+)"', ds_relat_tecnico)

            login = login_match.group(1) if login_match else 'Login not found.'
            password = password_match.group(1) if password_match else 'Password not found.'

            if phone_number != 'Phone not found.':
                if send_sms(phone_number, login, password):
                    update_order_status(nr_sequencia)
                else:
                    print(f'Sequence {nr_sequencia}: SMS not sent, skipping update.')
            else:
                print(f'Sequence {nr_sequencia}: Phone number not found.')

        cursor.close()
        connection.close()

    except cx_Oracle.DatabaseError as e:
        print(f"Database error: {e}.")

# Main loop to run the task every 5 minutes.
if __name__ == "__main__":
    while True:
        process_sql_results()
        time.sleep(300)  # Wait for 5 minutes (300 seconds).
