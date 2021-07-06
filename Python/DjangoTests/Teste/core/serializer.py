

from .models import Person, Admin, Evaluation
from rest_framework import serializers
from django.db.models import Avg

import json

# https://www.django-rest-framework.org/api-guide/relations/#serializer-relations


class AdminSerializer(serializers.ModelSerializer):

    age_herdado = serializers.SerializerMethodField()
    person = serializers.StringRelatedField(many=False)
    # many=False, pois como a relação é OneToOneField, não muitos campos
    # person, related_name da classe/Model Person
    # StringRelatedField retorna o método __str__ da classe que está recionalda ao related_name

    class Meta:
        model = Admin

        extra_kwargs = {
            'status': {'write_only': True}
        }

        fields = (
            'nome',
            'status',
            'age_herdado',
            'person',
        )

    def create(self, validated_data):
        adm = Admin.objects.create(**validated_data)
        return adm

    def get_age_herdado(self, obj):
        if hasattr(obj, 'person'):
            adm = obj.person.age
            return adm
        return 'Dado indisponível'

    def get_age_herdado(self, obj):
        print(Admin.objects.get(id=obj.id))
        adm = Admin.objects.get(id=obj.id)
        print(adm.person)
        return adm.person.age

    Forma de mostrar o status
    Como obj é um objeto com atributos nome e status, uma forma de passar o status
    é: return obj.status
    def get_status(self, obj):
        age = obj.status
        return age
        



class EvaluationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Evaluation

        fields = (
            'name',
            'comment',
            'grade',
        )

    def create(self, validated_data):
        return Evaluation.objects.create(**validated_data)


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

    A abordagem nested relation (evaluation = EvaluationSerializer(many=True, read_only=True)),
    precisa que a classe que se está buscando esteja serializada antes, para que possa ser usada


    class Meta:
        model = Person
        fields = (
            'name',
            'person_name',
            'age',
            'status_herdado',
            'evaluation',
        )


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


    def create(self, validated_data):
        person = Person.objects.create(**validated_data)

        Não é necessário dar um pop no dicionário para tirar o campo status_herdado,
        isso porquê esse campo não é uma chave, dessa forma é possível usar o método
        get_status_herdado sem problemas, inclusive sem declara o método create. Deixando
        ele ser criado de forma automática com o uso do ModelSerializer.

        return person

    def get_person_name(self, obj):
        name = obj.name.nome
        return name

    def get_status_herdado(self, obj):
        status = obj.name.status
        return status


