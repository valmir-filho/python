# Imports.
import cx_Oracle
import requests
from requests.auth import HTTPBasicAuth
import time

# DB homologation connection details.
host = ''
port = ''
service_name = ''
db_username = ''
db_password = ''

# API URL.
api_url = ''

# API authentication credentials.
api_username = ''
api_password = ''

# Prompts the user for their CPF and validates the input.
while True:
    print()
    cpf_user = input("Informe o seu CPF (apenas números): ")
    
    # Checks if the CPF contains only numbers and has exactly 11 characters.
    if cpf_user.isdigit() and len(cpf_user) == 11:
        break
    else:
        print("CPF inválido! Certifique-se de digitar apenas 11 números.")

# Create the connection string (DSN) for DB.
dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)

try:
    # Connect to the DB.
    connection = cx_Oracle.connect(user=db_username, password=db_password, dsn=dsn_tns)

    # Create a cursor.
    cursor = connection.cursor()

    # Define the SQL query to get user data.
    sql_query = """
    SELECT u.nm_usuario, u.ds_senha, u.ds_tec, p.nr_telefone_celular
    FROM usuario u
    JOIN pessoa_fisica p ON u.cd_pessoa_fisica = p.cd_pessoa_fisica
    WHERE p.nr_cpf = :cpf
    """

    # Execute the query with the CPF provided by the user.
    cursor.execute(sql_query, cpf=cpf_user)

    # Fetch the results.
    row = cursor.fetchone()

    if row:
        # Capture the data.
        username = row[0]
        cellphone = row[3]

        # Prepare the PL/SQL procedure call.
        plsql = """
        BEGIN
            feas_altera_senha(:ds_login_p, :senha_out);
        END;
        """

        # Define the output parameter.
        senha_out = cursor.var(cx_Oracle.STRING)

        # Execute the procedure.
        cursor.execute(plsql, ds_login_p=username, senha_out=senha_out)

        # Capture the generated password.
        generated_password = senha_out.getvalue()

        # Check if the phone number already contains the area code "41".
        if not cellphone.startswith("41"):
            cellphone = "41" + cellphone

        # Prepare the data to send the SMS.
        sms_data = {
            "codigo_carteira": "",
            "codigo_fornecedor": "",
            "envios": [
                {
                    "numero": cellphone,
                    "mensagem": f"""Sua senha temporária é: {generated_password}
Por favor, altere-a no próximo acesso ao Tasy.
A nova deve conter pelo menos 1 letra e 1 número."""
                }
            ]
        }

        # Making the POST request to send the SMS.
        try:
            response = requests.post(api_url, json=sms_data, auth=HTTPBasicAuth(api_username, api_password), timeout=10)

            # Check the response status.
            if response.status_code == 200:
                print()
                print(f'SMS enviado com sucesso para o número: {cellphone}')
                print()
                print(f'Celular errado? Entre em contato com a TI (9999-9999) para resetar a sua senha.')
            else:
                print('Failed to send SMS:', response.status_code)
                print('Details:', response.text)

        except requests.exceptions.RequestException as e:
            print('Error sending SMS:', e)
    else:
        print("No record found for the provided CPF.")

    # Close the cursor and connection.
    cursor.close()
    connection.close()

except cx_Oracle.DatabaseError as e:
    print(f"Error connecting to Oracle or executing the query: {e}")

time.sleep(15)
