from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    table_name = forms.CharField(max_length=100)  # Adicione os campos necessários
    db_name = forms.CharField(max_length=100) 