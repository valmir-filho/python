# Imports.
import cx_Oracle
import requests
from requests.auth import HTTPBasicAuth

# DB production connection details.
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

# Base URL do Google Forms (fixo).
forms_base_url = "https://docs.google.com/forms/*****/viewform?usp=pp_url&entry.420279824="

# DDD padrão (ex.: 41 para Curitiba).
ddd = '41'


# Função para enviar SMS.
def send_sms(cellphone, nr_atendimento):
    # Adiciona o DDD e código do Brasil.
    full_number = f"55{ddd}{cellphone}"

    # Monta a URL personalizada com o atendimento.
    forms_url = f"{forms_base_url}{nr_atendimento}"

    sms_data = {
        "codigo_carteira": "",
        "codigo_fornecedor": "",
        "envios": [
            {
                "numero": full_number,
                "mensagem": f"Hospital do Idoso Zilda Arns\nOla! Sua opiniao e muito importante para nos.\nParticipe da nossa pesquisa de satisfacao sobre o seu atendimento e nos ajude a melhorar.\nAcesse: {forms_url}"
            }
        ]
    }

    try:
        response = requests.post(api_url, json=sms_data, auth=HTTPBasicAuth(api_username, api_password), timeout=10)

        if response.status_code == 200:
            print(f"SMS enviado com sucesso para {full_number}.")
            print("Resposta:", response.text)
        else:
            print(f"Falha ao enviar SMS ({response.status_code}): {response.text}.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar SMS: {e}")


def main():
    dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)

    try:
        connection = cx_Oracle.connect(user=db_username, password=db_password, dsn=dsn_tns)
        cursor = connection.cursor()

        # Consulta Oracle.
        sql_query = """
        SELECT a.nr_atendimento,
               pf.nr_telefone_celular AS celular
          FROM atendimento_paciente_v a
         INNER JOIN pessoa_fisica pf
                 ON pf.cd_pessoa_fisica = a.cd_pessoa_fisica
         WHERE a.ie_tipo_atendimento = 1
           AND a.nr_seq_classificacao <> 1
           AND a.dt_cancelamento IS NULL
           AND a.cd_classif_setor IN (1,2,3,4,5)
           AND a.cd_estabelecimento = 1
           AND TRUNC(a.dt_alta) = TRUNC(SYSDATE) - 10
           AND SUBSTR(pf.nr_telefone_celular, 1, 1) = '9'
         ORDER BY 1
        """

        cursor.execute(sql_query)
        rows = cursor.fetchall()

        if not rows:
            print("Nenhum paciente encontrado para o critério.")
        else:
            for row in rows:
                nr_atendimento = row[0]
                cellphone = row[1]

                print(f"Enviando SMS para {cellphone} - Atendimento {nr_atendimento} ...")
                send_sms(cellphone, nr_atendimento)

        cursor.close()
        connection.close()

    except cx_Oracle.DatabaseError as e:
        print("Erro no Oracle:", e)


if __name__ == "__main__":
    main()
