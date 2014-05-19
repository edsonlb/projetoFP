""" 
@edsonlb
https://www.facebook.com/groups/pythonmania/
"""

from django.conf.urls import patterns, include, url

urlpatterns = patterns('caixas.views',
    url(r'^adicionar/$', 'caixaAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'caixaEditar'),
    url(r'^salvar/$', 'caixaSalvar'),
    url(r'^pesquisar/$', 'caixaPesquisar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'caixaExcluir'),
    url(r'^$', 'caixaListar'),

    url(r'^fluxo/$', 'caixaFluxo'),
    url(r'^fluxo/busca/$', 'fluxodecaixa'),
    url(r'^fluxo/relatorio/$', 'fluxodecaixa'),

    url(r'^pagamento/(?P<pk>\d+)/$', 'meu_pagamento'),
)