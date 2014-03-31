from django.conf.urls import patterns, include, url

urlpatterns = patterns('pessoas.views',
    url(r'^adicionar/$', 'pessoaAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'pessoaEditar'),
    url(r'^salvar/$', 'pessoaSalvar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'pessoaExcluir'),
    url(r'^$', 'pessoaListar'),
)