from django.shortcuts import render, redirect

from . import basededados
from .forms import ClienteForm


def index(request):
    """View da página inicial (index) da aplicação."""

    context = {}

    return render(request, 'index.html', context=context)


def clientes(request):
    """View da página de clientes: mostra os clientes registados e permite
    registar um novo através do procedimento armazenado na base de dados."""

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            basededados.inserir_cliente(
                form.cleaned_data['nome'],
                form.cleaned_data['nif'],
            )
            return redirect('clientes')
    else:
        form = ClienteForm()

    context = {
        'form': form,
        'clientes': basededados.listar_clientes(),
    }

    return render(request, 'clientes.html', context=context)