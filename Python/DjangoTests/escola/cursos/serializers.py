from rest_framework import serializers
from .models import Curso, Avaliacao
from django.db.models import Avg


class AvalicaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = { # determina que o email não vai ser apresentado
            'email': {'write_only': True}
        }
        # determina que o email não vai ser apresentado (na hora da consulta), vai ser exigido apenas
        # na hora do cadastro
        model = Avaliacao
        # o model serizalizer que vai ser apresentado é o model Avaliacao
        # que está no arquivo models.py
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
            # campos que serão apresentados quando a api for consultada
        )

    # VALIDAÇÃO A NÍVEL DE CAMPO
    # criando um método para validar as notas das avaliações
    # por pradão coloca-se validate_campoQueEstáSendoValidado
    # validate já é do próprio django, por isso a variável value(ou qualquer outro nome para ela)
    # já é buscada de forma automática, sem precisar fazer qualquer relação ou integração
    # se fosse necessário validar outros campos:
    # def validate_email(self, email): email já viria de forma automática
    # def validate_curso(self, curso): curso já viria de forma automática
    # def validate_nome(self, nome): nome já viria de forma automática
    def validate_avaliacao(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError('O valor precisa ser um inteiro de 1 a 5.')


class CursoSerializer(serializers.ModelSerializer):
    """
    Abordagem NESTED RELATIONSHIP

    Se a abordagem for 1 para 1 a Nested Relantionship é ideal
    Apesar de funcionar também com 1 para muitos, nesse caso ela não é indicada

    # Neste Relationship: relação 1 para muitos, por isso many=True
    # serão várias avaliações para muitos cursos
    avaliacoes = AvalicaoSerializer(many=True, read_only=True)

    """

    """
    Abordagem HYPERLINKED RELATED FIELD
    Abordagem 1 para 1, 1 para muitos, etc. 
    No caso dessa API, cria um link para cada avaliação
    
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='avaliacao-detail')
        # view_name, avaliacao vem do nome da model Avaliacao, tem no mesmo nome só com inicial minúscula
        # detail detalha cada avaliação
    
    """

    """
    Primary Key Related field
    
    Devolve o id do que está relacionado. Ex: estamos buscando o que está relacionado 
    com o curso, o que está relacionado com o curso é a avaliação, então o primary key
    traz o id das avaliações relacionadas com aquele curso
    """
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    media_avaliacoes = serializers.SerializerMethodField()
    # serializers.SerializerMethodField() vai se conectar ao get_media_avaliacoes automaticamente
    # pelo _media_avaliacoes, sem precisar passar argumentos.

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        """
        get_: assim como no validate, get_ é padrão, get_campoDesejado. Dessa forma 'obj' já vem por padrão automaticamente
        obj: vai ser o curso em questão do qual vem todas as avaliações
        avaliacoes: vem de related_name na model Avaliacoes
        aggregate: função de agregação, estudada em django e banco de dados 
        Avg('avaliacao'): vai fazer a média das avaliações, o campo 'avaliacao'(vindo do atributo avalicao da model) significa que é passado cada avaliação
        get('avaliacao__avg'): pega a média gerada por Avg('avaliacao')
        """
        if media is None:
            return 0
        return round(media * 2) / 2
    """
    essa abordagem seria mais eficiente se fosse feita um campo média de curso na model Curso
    pois toda vez que a requisição é feita a def get_media_avaliacoes é executada. Se houverem
    10000 avaliações,por exemplo, o sistema ficaria lento. Criado na model, o campo média só seria
    atualizado se uma nova avaliação fosse inserida. Fazer utilizando Signals. 
    """
