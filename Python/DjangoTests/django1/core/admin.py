from django.contrib import admin

from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque') # as variáveis aqui deve ter o mesmo nome que está na classe
                                                # Produto, do arquivo models(nome, preco e estoque)

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente)



