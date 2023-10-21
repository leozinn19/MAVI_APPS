from django.shortcuts import render
from django.conf import settings
from django.db import connection

def index(request):
    return render(request, 'index.html')

def list_databases(request):
    with connection.cursor() as cursor:
        cursor.execute("SHOW DATABASES")
        dbs= cursor.fetchall()
    
    return render(request, 'databases.html', {'dbs': dbs})

def list_tables(request, db_name):
    with connection.cursor() as cursor:
        cursor.execute(f"USE {db_name}")
        cursor.execute("SHOW TABLES")
        tabelas = cursor.fetchall()
    
    return render(request, 'tables.html', {'tabelas': tabelas})



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