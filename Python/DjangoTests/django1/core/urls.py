# Criando a url da aplicação
from django.urls import path # criando o caminho para se comunicar com a url do projeto
from .views import index, contato # impotando de views as funções
# from django.urls import path
from .views import index, contato, produto
# nos exemplos ele usou os 2 imports para funcionar, aqui não foi necessário, mas caso
# algum problema surja, usar os imports

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato),
    path('produto/<int:pk>', produto, name='produto')
    # criando rota para produto/<int:id>, do tipo int. Mando para uma view chamada produto
    # name='produto', o nome dessa rota é 'produto'.
    # A parte produto/<int:pk>/ especifica um padrão de URL:
    # produto/ significa apenas que a URL deve começar com a palavra produto seguida por /.
    # <int:pk> – essa parte é um pouco mais complicada. Ela nos diz que o Django espera um objeto do tipo inteiro e que vai transferi-lo para a view como uma variável chamada pk
    # por isso na view é necessário além do request, o pk.
    # o nome pk deve ser o mesmo na view.
]