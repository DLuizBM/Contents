from django.contrib import admin
from .models import Servicos, Cargo, Funcionario, Features


@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('servico', 'ativo', 'icone', 'modificado')


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'criados')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'criados', 'modificado')

@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('caracteristica', 'icone', 'ativo', 'criados', 'modificado')