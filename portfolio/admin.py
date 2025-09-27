# portfolio/admin.py

from django.contrib import admin
from .models import Projeto  # Importa o nosso modelo

# Garanta que esta linha existe e está correta
admin.site.register(Projeto)