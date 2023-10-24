from django.shortcuts import render
from django.conf import settings
from django.db import connection
from .form import UploadFileForm
from django.http import HttpResponse
from django.shortcuts import redirect

import pandas as pd

from .services.list_tables import tables
from .services.import_edit import import_edit
from .services.save_table import save_table
from .services.append_data import append_data, get_auto_increment_columns
from .services.aply_edit import aplicar_edicoes_service

def index(request):
    return render(request, 'index.html')

def list_databases(request):
    with connection.cursor() as cursor:
        cursor.execute("SHOW DATABASES")
        dbs= cursor.fetchall()
    
    return render(request, 'databases.html', {'dbs': dbs})

def list_tables(request, db_name):
    tabelas = tables(db_name)
    return render(request, 'tables.html', {'tabelas': tabelas, 'db_name': db_name})

def view_table(request, table_name, db_name):
    return render(request, 'view_table.html', {'table_name': table_name, 'db_name': db_name})


def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')

        # Verifica se as credenciais são válidas (implemente sua própria lógica de autenticação)
        try:
                # Atualiza as configurações do banco de dados
                settings.DATABASES['default']['USER'] = user
                settings.DATABASES['default']['PASSWORD'] = password
                return list_databases(request)
        except Exception as e:
                error_message = f"Erro ao conectar ao banco de dados: {e}"

        return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def save_table_to_excel(request, table_name, db_name):
    response = save_table(table_name, db_name) 
    return response

def append_excel(request, table_name, db_name):
    
    form = UploadFileForm(request.POST, request.FILES)
    if request.POST:
        print('CORRETO') 
        file = request.FILES['file']
        auto_increment = get_auto_increment_columns(table_name, db_name)
        append_data(table_name, db_name, file, auto_increment)

    return render(request, 'upload_file.html', {'form': form, 'table_name': table_name, 'db_name': db_name})

def edit_data(request, table_name, db_name):
    
    return render(request, 'edit.html', {'table_name': table_name, 'db_name': db_name})

def import_data(request, table_name, db_name):
    _import = import_edit(table_name, db_name)
    return _import

def apply_edit(request,table_name,db_name):
    form = UploadFileForm(request.POST, request.FILES)
    file = request.FILES['file']
    aplicar_edicoes_service(table_name, db_name, file)

    return render(request, 'edit.html', {'table_name': table_name, 'db_name': db_name})
