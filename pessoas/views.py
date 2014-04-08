from django.shortcuts import render, HttpResponseRedirect
from pessoas.models import Pessoa

def index(request):
    return render(request, 'index.html')

def pessoaListar(request):
    pessoas = Pessoa.objects.all()[0:10]
    # TESTE LOCAL PARA VERIFICAR SE A TABELA ESTA LISTANDO
    #pessoas = []
    #pessoas.append(Pessoa(nome='UNIFRAN', email='MAIL'))
    #pessoas.append(Pessoa(nome='CRUZEIRO'))
    return render(request, 'pessoas/listaPessoas.html', {'pessoas': pessoas})

def pessoaAdicionar(request):
    return render(request, 'pessoas/formPessoas.html')





















def pessoaSalvar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '0')

        try:
            pessoa = Pessoa.objects.get(pk=codigo)
        except:
            pessoa = Pessoa()

        pessoa.nome = request.POST.get('nome', '')
        pessoa.email = request.POST.get('email', '')
        pessoa.telefone = request.POST.get('telefone', '(00) 0-0000-0000')
        pessoa.logradouro = request.POST.get('logradouro', '')

        pessoa.save()
        return HttpResponseRedirect('/pessoas/')
