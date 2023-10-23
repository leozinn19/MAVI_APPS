from django.db import connection

def table_view(table_name, db_name):
    with connection.cursor() as cursor:
        cursor.execute(f"USE {db_name}")
        # Obtenha os nomes das colunas
        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = [row[0] for row in cursor.fetchall()]

        # Obtenha o conteúdo da tabela
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

    return columns, rows