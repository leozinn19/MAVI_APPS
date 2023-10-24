import pandas as pd
from django.db import connection

def aplicar_edicoes_service(table_name, db_name, file):
    excel_file = pd.read_excel(file)
    primary_key = f'cod_{table_name}'
    i = 0
    changes = 0
    with connection.cursor() as cursor:
        cursor.execute(f"USE {db_name}")
        updated_data_message = "DADOS ATUALIZADOS:<br>"
        for _, row in excel_file.iterrows():
            primary_key_column = row[primary_key]
            cursor.execute(
                "SELECT * FROM {} WHERE {} = %s".format(table_name, primary_key), (primary_key_column,))
            resultado = cursor.fetchone()
            print(i)
            if resultado:
                produto_banco = dict(zip([column[0] for column in cursor.description], resultado))
                produto_excel = row.to_dict()
                diferenca = {k: v for k, v in produto_excel.items(
                ) if pd.notnull(v) and produto_banco[k] != v}
                if diferenca:
                    changes = changes +1
                    set_clause = ', '.join(
                        [f"{k} = %s" for k in diferenca.keys()])
                    cursor.execute(
                        f"UPDATE {table_name} SET {set_clause} WHERE {primary_key} = %s", (*diferenca.values(), primary_key_column))
                    updated_data_message += f"{primary_key}: {primary_key_column} - Campos atualizados: {diferenca}<br>"
            i= i+1
        if changes==0:
            updated_data_message += f'Não foi realizada nenhuma edição na tabela {table_name}'
        
