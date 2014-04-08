from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length='100', 
        blank=False, 
        null=False)

    email = models.CharField(max_length='100', 
        blank=True, 
        null=True)

    telefone = models.CharField(max_length='20', 
        blank=True, 
        null=True)

    logradouro = models.CharField(max_length='200', 
        blank=True, 
        null=True)
