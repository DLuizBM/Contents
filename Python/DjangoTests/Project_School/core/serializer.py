from .models import Admins, Employees, Address, Document
from rest_framework import serializers


class AdminsSerializer(serializers.ModelSerializer):

    admin_name = serializers.SerializerMethodField()

    class Meta:
        model = Admins
        fields = (
            'name',
            'admin_name',
            'bio',
        )

    def get_admin_name(self, object):
        name = object.name.username
        return name


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'country',
            'state',
        )


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            'type',
            'number',
        )


class EmployeesSerializer(serializers.ModelSerializer):

    # funcionando
    address = AddressSerializer()
    #email = serializers.CharField()

    document = DocumentSerializer()

    class Meta:
        model = Employees

        fields = (
            'name',
             #'email',
            'birthday',
            'id_number',
            'address',
            'document',
        )

    def create(self, validated_data):
        validated_data2 = validated_data.copy()
        # sem copiar o dicionário, o dicionário muda de tamanho ao longo da iteração
        # por isso é feito uma cópia para se trabalhar
        for key in validated_data:
            if key == "address":
                address_data = validated_data2.pop(key)
            if key == "document":
                document_data = validated_data2.pop(key)

        employee = Employees.objects.create(**validated_data2)

        Address.objects.create(user=employee, **address_data)
        Document.objects.create(user=employee, **document_data)
        return employee

    """
    # funcionando para 2 atributo no address, country, state
    def create(self, validated_data):
        print('Aqui está o validated_data:', validated_data)

        address_data = validated_data.pop('address')
        print('Aqui está o address_data:', address_data)

        employee = Employees.objects.create(**validated_data)
        print('Aqui está o employee 1:', employee)

        print('Aqui está o employee 2 :', Address.objects.create(user=employee, **address_data))
        return employee
    """
    """
    Aqui está o validated_data: {'name': <User: divinoluiz>, 'birthday': '01/08/1998', 'id_number': '1234567', 'address': OrderedDict([('country', 'EUA'), ('state', 'Nova Iorque')])}
    Aqui está o address_data: OrderedDict([('country', 'EUA'), ('state', 'Nova Iorque')])
    Aqui está o employee 1: divinoluiz
    Aqui está o employee 2 : divinoluiz


    """