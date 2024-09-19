import cx_Oracle
import requests
from requests.auth import HTTPBasicAuth
import tkinter as tk
from tkinter import ttk, messagebox

# DB homologation connection details.
host = ''
port = ''
service_name = ''
db_username = ''
db_password = ''

# API URL.
api_url = 'https://api360.classeaservicos.com.br/api/send.php'

# API authentication credentials.
api_username = ''
api_password = ''

# Function to mask the phone number.
def mask_phone_number(phone_number):
    # Keep the first 2 and last 4 digits, replacing the middle with asterisks.
    return phone_number[:2] + "****" + phone_number[-4:]

# Function to process the CPF and perform the necessary operations.
def process_cpf(cpf_user):
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

        # Execute the query with the provided CPF.
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
A nova deve conter 6 caracteres com pelo menos 1 letra e 1 número."""  # Message format.
                    }
                ]
            }

            # Making the POST request to send the SMS.
            try:
                response = requests.post(api_url, json=sms_data, auth=HTTPBasicAuth(api_username, api_password), timeout=10)

                # Check the response status.
                if response.status_code == 200:
                    show_success_message(cellphone)
                else:
                    messagebox.showerror("Error", f'Failed to send SMS: {response.status_code}\nDetails: {response.text}')

            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f'Error sending SMS: {e}')
        else:
            messagebox.showerror("Erro!", "Registro não encontrado para o CPF fornecido.")

        # Close the cursor and connection.
        cursor.close()
        connection.close()

    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Error", f"Error connecting to Oracle or executing the query: {e}")

# Function to show the success message.
def show_success_message(cellphone):
    # Mask the phone number.
    masked_phone_number = mask_phone_number(cellphone)
    
    # Show the success message and close all windows on OK.
    if messagebox.showinfo(
        "Success",
        f'Senha enviada com sucesso para o celular final: {masked_phone_number}\n\n'
        'Não recebeu a senha? Ligue para a TI: 3316-5999.'
    ):
        root.destroy()  # Close the application immediately after user clicks OK.

# Function to validate the CPF and start the process.
def validate_and_process_cpf(event=None):
    cpf_user = cpf_entry.get()
    
    # Validate the CPF (only numbers and 11 digits).
    if cpf_user.isdigit() and len(cpf_user) == 11:
        process_cpf(cpf_user)
    else:
        messagebox.showerror("Erro", "CPF inválido! Certifique-se de digitar apenas os 11 números.")

# Function to validate the input.
def validate_input(P):
    if P.isdigit() or P == "":
        return True
    return False

# GUI configuration using Tkinter.
root = tk.Tk()
root.title("🔐 Alteração de Senha do Tasy 🔐")

# Define the window size and center it on the screen.
window_width = 450
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Configure styles with larger fonts.
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 14), padding=10)
style.configure('TLabel', font=('Helvetica', 14))
style.configure('TEntry', font=('Helvetica', 14))

# Create a validation method for CPF entry.
vcmd = root.register(validate_input)

# Main frame to center the widgets.
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(expand=True)

# Label and entry field for CPF.
cpf_label = ttk.Label(main_frame, text="Por favor, Informe o número do seu CPF:")
cpf_label.pack(pady=10)

cpf_entry = ttk.Entry(main_frame, width=30, justify='center', validate='key', validatecommand=(vcmd, '%P'))
cpf_entry.pack(pady=10)
cpf_entry.bind('<Return>', validate_and_process_cpf)  # Bind the Enter key to submit the CPF.

# Button to continue.
submit_button = ttk.Button(main_frame, text="Continue", command=validate_and_process_cpf)
submit_button.pack(pady=20)

# Run the GUI loop.
root.mainloop()
