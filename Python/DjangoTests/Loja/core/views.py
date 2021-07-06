from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import Carro, Marca


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['MARCAS'] = Marca.objects.all()
        return context


class ToyotaView(TemplateView):
    template_name = 'toyota.html'

    def get_context_data(self, **kwargs):
        context = super(ToyotaView, self).get_context_data(**kwargs)
        context['CARROS'] = Carro.objects.all()
        return context


class HondaView(TemplateView):
    template_name = 'honda.html'

    def get_context_data(self, **kwargs):
        context = super(HondaView, self).get_context_data(**kwargs)
        context['CARROS'] = Carro.objects.all()
        return context


class VolksView(TemplateView):
    template_name = 'volkswagen.html'

    def get_context_data(self, **kwargs):
        context = super(VolksView, self).get_context_data(**kwargs)
        context['CARROS'] = Carro.objects.all()
        return context