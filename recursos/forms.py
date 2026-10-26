from django import forms


class ClienteForm(forms.Form):

    nome = forms.CharField(label='Nome', max_length=100)
    nif = forms.CharField(label='NIF', max_length=9, min_length=9)
