import cx_Oracle
import time
from plyer import notification  # Importing the notification module from plyer.

# Database connection details for the production environment.
host = ''
port = ''
service_name = ''
db_username = ''
db_password = ''

# Create the Data Source Name (DSN) string required for Oracle connections.
dsn_tns = cx_Oracle.makedsn(host, port, service_name)

def check_orders():
    """Connect to the database, run the query, and return the count of pending orders."""
    try:
        # Connect to the Oracle database using provided credentials.
        conn = cx_Oracle.connect(db_username, db_password, dsn_tns)
        # Use a cursor to execute SQL queries.
        with conn.cursor() as cursor:
            # SQL query to count pending service orders that match specific criteria.
            query = """
            SELECT COUNT(*) 
            FROM MAN_ORDEM_SERVICO mo
            INNER JOIN pessoa_fisica pf ON pf.cd_pessoa_fisica = mo.CD_PESSOA_SOLICITANTE
            INNER JOIN MAN_LOCALIZACAO ml ON ml.NR_SEQUENCIA = mo.NR_SEQ_LOCALIZACAO
            INNER JOIN MAN_GRUPO_TRABALHO mg ON mg.NR_SEQUENCIA = mo.NR_GRUPO_TRABALHO
            WHERE mo.NR_GRUPO_PLANEJ = '11' 
              AND mo.IE_STATUS_ORDEM = '1' 
              AND mo.NR_GRUPO_TRABALHO IN (2, 91) 
              AND mo.NM_USUARIO_EXEC IS NULL
              AND mo.DT_INICIO_DESEJADO > TRUNC(SYSDATE)
            """
            # Execute the query.
            cursor.execute(query)
            # Fetch the first row of the result (the count of orders).
            result = cursor.fetchone()
            count = result[0]
            return count
    except cx_Oracle.DatabaseError as e:
        # Handle any errors during the database connection or query execution.
        print(f"Error connecting to the database: {e}.")
        return 0
    finally:
        # Ensure the database connection is closed after the operation.
        if conn:
            conn.close()

def generate_system_notification(count):
    """Generate a system notification if there are pending service orders."""
    if count == 1:
        # Construct the message for a single pending service order.
        message = f"Atenção! Existe {count} ordem de serviço não iniciada."
    elif count > 1:
        # Construct the message for multiple pending service orders.
        message = f"Atenção! Existem {count} ordens de serviços não iniciadas."
    
    # Show the notification using plyer.
    notification.notify(
        title="Notificador de Ordens de Serviço do Tasy",
        message=message,
        timeout=10  # Notification will last for 10 seconds.
    )

# Main loop: Check for pending orders every 5 minutes (300 seconds).
while True:
    # Get the number of pending orders by calling the check_orders function.
    count = check_orders()
    
    # Generate a notification if there are pending orders.
    generate_system_notification(count)
    
    # Wait for 300 seconds (5 minutes) before checking again.
    time.sleep(300)
