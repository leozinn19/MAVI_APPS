from django.urls import path
from cubo_data.views import index, login, list_tables, list_databases
urlpatterns = [
    path("", index),
    path("login/", login, name='login'),
    path("databases/", list_databases, name='dbs'),
    path('tables/<str:db_name>/', list_tables, name='tables'),
]
