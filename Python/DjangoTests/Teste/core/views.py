from django.shortcuts import render
from rest_framework import viewsets
from .models import Person, Admin, Evaluation
from .serializer import PersonSerializer, EvaluationSerializer, AdminSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import IsAutenticated
from rest_framework import permissions
# Create your views here.


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = (IsAutenticated,)

    @action(detail=True, methods=['get'])
    def pperson(self, request, pk=None):
        ps = self.get_object()
        print(f'age:', ps.person.age)
        serializer = PersonSerializer(ps.person)
        return Response(serializer.data)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (permissions.DjangoModelPermissions, )
    # permissions faz com que o usuário esteja sujeito as configurações impostas no Django model
    # logo, para acessar essa view deve ser autenticado

    @action(detail=True, methods=['get'])
    def evaluation(self, request, pk=None):
        evaluate = self.get_object()
        print(evaluate)
        # Luiz
        serializer = EvaluationSerializer(evaluate.evaluation.all(), many=True)
        print('Serializer', serializer.data)
        # Serializer[OrderedDict([('name', 4), ('comment', 'Awesome!!'), ('grade', '100.00')])]
        return Response(serializer.data)

    def get_queryset(self):

        person = super().get_queryset()
        """
        person = super().get_queryset().filter(id=4)
        filter != get
        filter(id=4) : <QuerySet [<Person: Luiz>]>
        get(id=4) : <Person: Luiz>

        O retorno deve ser um QuerySet, e não apenas a Model <Person>. Usando o get será apresentado erro.
        """

        qs = person
        return qs




    """
    def get_queryset(self):
        if self.request.method == 'GET':
            # queryset = Person.objects.all()
            print(self.request.get_host())
            # print(dir(self))
            print(f'Super().get_queryset', super().get_queryset())
            print(f'Person.objects.all()', Person.objects.all())
            print(f'Self.queryset', self.queryset)
            return Person.objects.all()
            
    """



class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

