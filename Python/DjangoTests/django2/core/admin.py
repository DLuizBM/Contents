from django.contrib import admin
from .models import Produto

# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')
    # os nomes aqui devem ser iguais as das variáveis na classe Produto da model
    # na página será mostrado a string definida em cada variável
    # ex: chamanda a variável modificado, na página será mostrado 'Data de atualização'
    # tudo em maiúsculo
