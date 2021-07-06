from core.models import Admin
from rest_framework import serializers


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

    """
    def get_age_herdado(self, obj):
        print(Admin.objects.get(id=obj.id))
        adm = Admin.objects.get(id=obj.id)
        print(adm.person)
        return adm.person.age
        """
    """
    Forma de mostrar o status
    Como obj é um objeto com atributos nome e status, uma forma de passar o status
    é: return obj.status
    def get_status(self, obj):
        age = obj.status
        return age

    """

