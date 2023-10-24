from django.urls import path
from cubo_data.views import ( index, login, list_tables, list_databases, view_table, save_table_to_excel, 
                             append_excel, edit_data, import_data, apply_edit )
urlpatterns = [
    path("", index),
    path("login/", login, name='login_page'),
    path("databases/", list_databases, name='dbs'),
    path('tables/<str:db_name>/', list_tables, name='tables'),
    path('view_table/<str:table_name>/<str:db_name>', view_table, name='view_table'),
    path('save_table/<str:table_name>/<str:db_name>', save_table_to_excel, name='save_table'),
    path('upload_file/<str:table_name>/<str:db_name>', append_excel, name='upload_file'),
    path('edit_file/<str:table_name>/<str:db_name>', edit_data, name='edit_data'),
    path('import_data/<str:table_name>/<str:db_name>/', import_data, name='import_data'),
    path('apply_edit/<str:table_name>/<str:db_name>/', apply_edit, name='apply_edit'),
]
