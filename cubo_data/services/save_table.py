import io
import pandas as pd 

from django.db import connection
from django.http import HttpResponse

def save_table(table_name, db_name):
    with connection.cursor() as cursor:
        cursor.execute(f"USE {db_name}")
        
        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = [row[0] for row in cursor.fetchall()]

        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        df = pd.DataFrame(rows, columns=columns)
        excel_file = io.BytesIO()
        df.to_excel(excel_file, index=False, sheet_name='Tabela')
        response = HttpResponse(
        excel_file.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        file_name = f"{table_name.upper()}_{db_name.lower()}.xlsx"
        response['Content-Disposition'] = f'attachment; filename={file_name}'

    return response