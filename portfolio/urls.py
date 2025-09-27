# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # A string vazia '' significa a página inicial
    path('', views.home, name='home'),
]