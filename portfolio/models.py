# portfolio/models.py
from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologia = models.CharField(max_length=50)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo