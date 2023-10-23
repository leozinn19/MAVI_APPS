from django.db import connection

def tables(db_name):
    with connection.cursor() as cursor:
        cursor.execute(f"USE {db_name}")
        cursor.execute("SHOW TABLES")
        tabelas = cursor.fetchall()
    
    return tabelas