"""
Essa view não será mais utilizada, pois a forma como foi criada não é a melhor.
Estará aqui apenas como histórico, a nova view será criada como generic view.

"""


from rest_framework.views import APIView
# API é o class based view do django rest
from rest_framework.response import Response
# Response prepara a resposta da requisição
# API view recebe a requisição e o response devolve a resposta
from rest_framework import status
# com esse método temos acesso a vários status do http

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvalicaoSerializer


class CusoAPIView(APIView):
    """
    API de cursos
    """
    # implementando o método HTTP get, esse método recebe uma requisição, um request
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        # cursos recebe todos os objetos, serializer recebe todos os objetos transformados
        # em JSON, por conta de CursoSerializer. Mas só os atributos que estão lá.
        # many = True, passa todos os objetos, informa que estão sendo passado muitos objetos
        print(serializer)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data) # pegando os dados que estão vindo na requisição
        # fazendo a requisição dos dados, serializando de volta do JSON pros objetos django
        serializer.is_valid(raise_exception=True)
        # verifica se os dados são válidos, se não, manda uma exceção
        serializer.save()
        print(f'Self.request.data', self.request.data)
        # salvando os dados no banco de dados
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # retornando os dados salvos e o status http


class AvaliacaoAPIView(APIView):
    """
    API de avaliações
    """
    # Todo cabeçalho da requisição está no request
    def get(self, request):
        print(request.user)
        avaliacao = Avaliacao.objects.all()
        serializer = AvalicaoSerializer(avaliacao, many=True)
        return Response(serializer.data)
        # Response trata e gera um JSON, serializer.data manda um dicionário python

    def post(self, request):
        serializer = AvalicaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



