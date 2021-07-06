from django.contrib import admin
from core.models import Marca, Carro


@admin.register(Marca)
class AdminMarca(admin.ModelAdmin):
    list_display = ('nome', 'criacao', 'modificacao')


@admin.register(Carro)
class AdminCarro(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'anomodelo', 'estado', 'quilometragem', 'motor', 'cambio', 'preco')




