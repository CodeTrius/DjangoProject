# portfolio/views.py
from django.shortcuts import render
from .models import Projeto # Importa o nosso modelo de dados

def home(request):
    # Busca todos os objetos 'Projeto' que estão salvos no banco de dados
    projetos = Projeto.objects.all()

    # Envia os projetos para o template dentro de um dicionário chamado 'contexto'
    contexto = {'projetos': projetos}

    # Renderiza (cria) a página HTML 'home.html' com os dados do contexto
    return render(request, 'portfolio/home.html', contexto)