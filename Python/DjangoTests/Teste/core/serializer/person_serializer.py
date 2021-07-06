from core.models import Person
from .evaluation_serializer import EvaluationSerializer
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):

    status_herdado = serializers.SerializerMethodField()
    person_name = serializers.SerializerMethodField()
    # 1 - evaluation = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # evaluation deve ter o mesmo nome do related_name, para se ter acesso a todos os atributos
    # da classe Evaluation. many para especificar que são muitos dados desse tipo e read_only
    # para que ele não interprete como sendo uma dados que precisa ser digitado e adicionado ao
    # validated_data.

    # 2 -  evaluation = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='evaluation-detail')
    # view-name= 'nome da model'-detail
    # Essas abordagens não necessitam que a classe esteja serializada antes
    evaluation = EvaluationSerializer(many=True, read_only=True)
    """
    A abordagem nested relation (evaluation = EvaluationSerializer(many=True, read_only=True)),
    precisa que a classe que se está buscando esteja serializada antes, para que possa ser usada
    """

    class Meta:
        model = Person
        fields = (
            'name',
            'person_name',
            'age',
            'status_herdado',
            'evaluation',
        )

    """
    def create(self, validated_data):
        print(self.context.get('request').user)
        print(self.context.get('request').method)
        print(self.context.get('view'))
        print(self.context)
        person = Person.objects.create(**validated_data)
        # importante
        print(person)
        # print(f'Self:', dir(self))
        print(f'Self.data:', self.data)
        # data devolve os dados do objeto analisado
        # Ex: cadastrado -> name: Ayrton Senna, age: 55
        # self.data: {'name': 'Ayrton Senna', 'age': '55'}

        return person
    """

    def create(self, validated_data):
        person = Person.objects.create(**validated_data)
        """
        Não é necessário dar um pop no dicionário para tirar o campo status_herdado,
        isso porquê esse campo não é uma chave, dessa forma é possível usar o método
        get_status_herdado sem problemas, inclusive sem declara o método create. Deixando
        ele ser criado de forma automática com o uso do ModelSerializer.
        """
        return person

    def get_person_name(self, obj):
        name = obj.name.nome
        return name

    def get_status_herdado(self, obj):
        status = obj.name.status
        return status


