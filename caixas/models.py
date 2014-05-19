from django.db import models
from pessoas.models import Pessoa

class Conta(models.Model):
    pessoa = models.ForeignKey(Pessoa)

    #E = Entrada / S = Saida
    tipo = models.CharField(db_index=True, max_length='1', blank=False, null=False) 

    descricao = models.CharField(db_index=True, max_length='200', blank=False, null=False)

    valor = models.DecimalField(max_digits=13, decimal_places=2, default=0)

    pagseguro = models.CharField(max_length='300', blank=True)

    data = models.DateTimeField(db_index=True, auto_now=False, auto_now_add=True)