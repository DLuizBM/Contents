from django.urls import path
from .views import (CursoAPIView,
                    AvaliacaoAPIView,
                    CursosAPIView,
                    AvaliacoesAPIView,
                    CursoViewSet,
                    AvaliacaoViewSet)

# from .views_old import CusoAPIView, AvaliacaoAPIView
# o método refactor trocou a referencia para .views_old
# mas essa é a view antiga, mudar para view para aparecer o formulário HTML
# na API.

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('CURSOS', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)


"""
A view AvaliacoesAPIView traz todas as avaliações disponíveis
A view AvaliacaoAPIView traz uma avaliacao quando se passa o id/pk
"""

urlpatterns = [

    path('curso/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('avaliacao/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
    # path('avaliacao/<int:pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
    # a forma antiga foi mudada para avaliaçao_pk pois um método dentro de AvaliacaoAPIView foi sobrescrito
    # informando a primary key pk, já que a RetrieveUpdateDestroy necessita de um id identificador
    # Quando se faz uso de class based views no DRF, ele espera que seja passado um dado chamado pk
    # esse identificador vai ser passado automaticamente pelas generic views

    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    # o endpoint 'avalicoes/' executa a view AvaliacoesAPIView.as_view()
    # deve-se informar a url do projeto que foi criado uma url na aplicação

    path('curso/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    # curso_pk: o pk é do curso e não da avaliação, por isso não foi necessário fazer alteração na linha 25
    # pois o pk aqui é de curso e não de avalição, diferente do que foi feito na linha 17, que foi necessária a mudança
    # pois no método abaixo, linha 33, usa-se avaliacao_pk, pk de avaliacao
    path('curso/<int:curso_pk>/avaliacao/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao')
    # Deixando explícito o pk do curso e o pk da avaliação que quero
    # http://127.0.0.1:8000/api/v1/curso/1/avaliacao/3
    # desejo consultar o curso de id/pk 1 e a avaliacao de id/pk 3 desse curso
]

