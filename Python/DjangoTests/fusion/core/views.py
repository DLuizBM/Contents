"""
ser = {'servico': 'automa', 'desc': 'oii'}, {'servico': 'design', 'desc': 'olaa'}
# criando uma tupla de dicionários (cada dicionário representa cada objeto vindo da classe)
cria = dict()
cria['serv'] = ser
# cria é um dicionário com a chave 'serv' e como valor uma tupla de dicionários
for s in cria['serv']:
    print(s['servico'])
    print(s['desc'])

"""
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import Servicos, Funcionario, Features
from .forms import ContatoForms
from django.contrib import messages
from django.urls import reverse_lazy

#class IndexView(TemplateView):


class IndexView(FormView):
    # essa alteração foi necessária pois a própria index tem um formulário de contato
    # se o formulário estivesse em outra página, então seria possível deixa a index como templateview
    # e criar outra classe para contato com formview
    template_name = 'index.html'
    form_class = ContatoForms
    success_url = reverse_lazy('index') # se o formulário é válido depois de submetido, retorna pra index

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # context['SERVICOS'] = Servicos.objects.all()
        context['SERVICOS'] = Servicos.objects.order_by('?').all()
        # 'SERVICOS' -> dicionário que é passado para o template e como deve ser chamado lá
        # envia os objetos de forma aleatória, mudando a ordem em que são apresentados
        print(context['SERVICOS'])
        # ler o comentário para entender como funciona o dicionário context
        # como ele recebe os dicionários da model e como ele passa para index
        context['FUNCIONARIOS'] = Funcionario.objects.all()
        context['CARACTERISTICAS'] = list(Features.objects.all())
        print(f'Queryset{Features.objects.all()[0:3:]}')
        # É possível fazer slicing em querysets também
        # inicia na posição 0 e vai até a posição 3-1
        print(list(Features.objects.all()))
        # é possível transformar uma QuerySet em lista e assim trabalhar como lista
        # como foi feito em features.html, que foi usado o recurso de slice
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()    # form.nome_da_função_definida_no_forms_que_envia_o_email()
        messages.success(self.request, 'E-mail enviado com sucesso.')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'E-mail não enviado.')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

    # form_valid e form_invalid são métodos que funcionam somente com class based views


class TestView(TemplateView):
    template_name = 'teste.html'
