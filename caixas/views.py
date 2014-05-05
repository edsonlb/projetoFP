# This Python file uses the following encoding: utf-8
# ANOTAÇÃO PARA USAR CARACTERES ESPECIAIS AQUI. (MESMO PARA ANOTAÇÕES.)
""" 
@edsonlb
https://www.facebook.com/groups/pythonmania/
"""

from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q #Queries complexas
from caixas.models import Conta
from pessoas.models import Pessoa

def caixaListar(request):
    contas = Conta.objects.all()[0:10]

    return render(request, 'caixas/listaCaixas.html', {'contas': contas})


def caixaAdicionar(request):
    pessoas = Pessoa.objects.all().order_by('nome')

    return render(request, 'caixas/formCaixas.html', {'pessoas': pessoas})

def caixaSalvar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '0')

        try:
            conta = Conta.objects.get(pk=codigo)
        except:
            conta = Conta()

        conta.pessoa_id = request.POST.get('pessoa_id', '1')
        conta.tipo = request.POST.get('tipo', '').upper()
        conta.descricao = request.POST.get('descricao', 'CONTA SEM DESCRIÇÃO').upper()
        conta.valor = request.POST.get('valor', '')
        conta.data = request.POST.get('data', '')

        conta.save()
    return HttpResponseRedirect('/caixas/')

def caixaPesquisar(request):
    if request.method == 'POST':
        textoBusca = request.POST.get('textoBusca', 'TUDO').upper()

        try:
            if textoBusca == 'TUDO':
                pessoas = Pessoa.objects.all()
            else: 
                pessoas = Pessoa.objects.filter(
                    (Q(nome__contains=textoBusca) |  
                    Q(email__contains=textoBusca) | 
                    Q(telefone__contains=textoBusca) | 
                    Q(logradouro__contains=textoBusca))).order_by('-nome')  #BUSCA POR NOME OU EMAIL OU TELEFONE OU LOGRADOURO... E É ORDENADO POR NOME.
        except:
            pessoas = []

        return render(request, 'caixas/listaCaixas.html', {'pessoas': pessoas, 'textoBusca': textoBusca})

def caixaEditar(request, pk=0):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except:
        return HttpResponseRedirect('/caixas/')

    return render(request, 'caixas/formPessoas.html', {'pessoa': pessoa})

def caixaExcluir(request, pk=0):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
        pessoa.delete()
        return HttpResponseRedirect('/caixas/')
    except:
        return HttpResponseRedirect('/caixas/')




    




