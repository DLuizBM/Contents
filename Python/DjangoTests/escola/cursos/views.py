"""
Para criar operações básicas de CRUD o ideal é usar generic views
Compara a quantidade de código escrito nessa view, com a views_old
A quantidade de código é muito menos

"""
from rest_framework import generics
# importando as generics para criar as generics views
from rest_framework.generics import get_object_or_404

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvalicaoSerializer

from rest_framework import viewsets
from rest_framework.decorators import action  # com action é possível alterar ações dentro do ModelView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions
from .permissions import IsSuperUser
"""
API V1
"""
class CursosAPIView(generics.ListCreateAPIView):
    # ListCreat: permite listar e criar, ou seja, pra listar(POST), para criar(POST)
    # já tenho esse métodos http disponíveis
    queryset = Curso.objects.all()
    # passando todos os objetos pro queryset
    serializer_class = CursoSerializer
    # informando qual a classe que vai serializar os objetos


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    # RetrieveUpdateDestroy: faz os métodos Update e delete
    # Retrieve...troy: precisa do id para poder identificar o objeto a ser deletado ou atualizado
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    # queryset vai ter todos os objetos
    serializer_class = AvalicaoSerializer

    # SOBRESCREVENDO O MÉTODO get_querset()

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            """
            self.kwargs pega os valores de id passado
            ex: http://127.0.0.1:8000/api/v1/avaliacao/1
            self.kwargs pega 1
            curso/<int:curso_pk>/avaliacoes/
            self.kwargs pega o <int:curso_pk>
            """
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
            # dentro de todos os objetos, self.queryset
            # se houver um valor em curso_pk, é feita uma filtragem para retornar as avaliações pelo curso
            # indicado pelo pk
        return self.queryset.all()
        # se não houver um valor em curso_pk, significa que está sendo feita uma consulta em todas as avalições


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvalicaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        # self.get_queryset() pega todos os objetos
        # self.kwargs.get('curso_pk') pega o curso_pk
        # dentro do curso_pk, self.kwargs.get('avaliacao_pk'), pega a avaliacao_pk (id com que ela foi
        # criada e não a ordem que ela está no curso)
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
        # get_object_or_404, pegue o objeto ou mande 404(objeto não encontrado)
        # se não houver curso_pk, retorna a avalicao_pk
#############################################################################################

"""
API V2
"""


class CursoViewSet(viewsets.ModelViewSet):
    """
    No arquivo settings.py, foi feita uma configuração de permissão global
    aqui com o permissiona_classes estamos fazendo uma permissão personalizada para essa view
    sendo assim, só terá permissão para usar o método GET para ver o/os cursos, o usuário
    autenticado.

    """
    permission_classes = (IsSuperUser, permissions.DjangoModelPermissions, )     # uma tupla de único elemento, por isso a vírgula
    # agora além de estar autenticado para acessar essa classe, caso o usuário queira deletar um curso
    # deve ser super usuário
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # o decorator é usado para criar essa rota(avaliacoes)
    # detail=True, cria a rota e methods especifica os métodos que terão acesso
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        print(f'Curso', curso)
        print(f'Dir(curso)', dir(curso.avaliacoes.all()))
        # o objeto self é o curso que está chamando essa url
        # ex: http://127.0.0.1:8000/api/v2/curso/1/, se curso com id 1 for "API's com DRF"
        # o objeto vai ser "API's com DRF"
        serializer = AvalicaoSerializer(curso.avaliacoes.all(), many=True)
        print('Serializer', serializer)
        print('Data', serializer.data)
        # curso.avaliacoes.all(): avaliacoes vem de related_name='avaliacoes' em models
        # pega todas as avaliações daquele curso em questão
        # relacionamento entre classes
        return Response(serializer.data)
        # ex de utilização http://127.0.0.1:8002/api/v2/CURSOS/5/avaliacoes/

"""
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvalicaoSerializer

# com viewsets apenas com esse trecho de código, foi feita toda a parte de CRUD da versão 1 da API
# Na api de versão 1, era possível fazer buscas:
# http://127.0.0.1:8000/api/v1/curso/1/avaliacoes/
# Na api v2, isso não é possível, pois o viewsets gera apenas as operações CRUD de um único model
# ou cursos ou avaliações, ou seja:
# http://127.0.0.1:8000/api/v2/curso/1/avaliacoes/, não seria possível, pois estamos fazendo
# o acesso a dois models
# O viewsets não gera isso de forma automática, deve ser construído.
"""

# E se não quisermos que a view set não liste todas as avaliações, como no caso anterior


class AvaliacaoViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin, # retrievie recupera dados ex: http://127.0.0.1:8000/api/v2/avaliacoes/2/, o objeto /2/ é recuperado pelo retrieve
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
                        # viewsets.GenericViewSet agrupa todos os anteriores

    # Para tirar uma das funcionalidades, basta comentar um dos seguintes métodos
    # ex: para tirar o método GET e não mais listar os objetos, basta comentar
    # mixins.ListModelMixin

    queryset = Avaliacao.objects.all()
    serializer_class = AvalicaoSerializer