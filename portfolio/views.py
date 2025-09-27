# portfolio/views.py
from django.shortcuts import render
from .models import Projeto # Importa o nosso modelo de dados

def home(request):
    projetos = Projeto.objects.all()

    contexto = {'projetos': projetos}

    return render(request, 'portfolio/home.html', contexto)