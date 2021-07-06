from django.contrib import admin
from .models import Carro


# admin.site.register(Carro) -> sem o decorator
@admin.register(Carro)
class CarrAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marcas', 'ano', 'motorizacao', 'quilometragem', 'estado', 'preco')

