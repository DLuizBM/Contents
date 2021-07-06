from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import Carro


class CarroView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(CarroView, self).get_context_data(**kwargs)
        context['CARROS'] = Carro.objects.all()
        return context


class ToyotaView(TemplateView):
    template_name = 'Toyota.html'

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
