from django.db import models
from stdimage import StdImageField
import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criacao = models.DateField('Data de criação', auto_now_add=True)
    modificacao = models.DateField('Data de modificação', auto_now=True)

    class Meta:
        abstract = True


class Marca(Base):
    nome = models.CharField('Marca', max_length=20)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'MARCAS'

    def __str__(self):
        return self.nome

    # def __str__ é importante para que se retorne o nome da marca
    # para a classe Carro, sem isso é retornado 'Marca object' e não o 'nome'
    # Retorna o nome da Marca na página admin em 'Recent Actions' - 'My actions'

class Carro(Base):
    ICONE_CHOICES = (
        ('Novo', 'Novo'),
        ('Usado', 'Usado'),
    )

    ICONE_CHOICES2 = (
        ('Automático', 'Automático'),
        ('Manual', 'Manual'),
    )

    marca = models.ForeignKey('core.Marca', verbose_name='Marca', on_delete=models.CASCADE)
    modelo = models.CharField('Modelo', max_length=20)
    ano = models.CharField('Ano de Fabricação', max_length=4)
    anomodelo = models.CharField('Ano de Modelo', max_length=4)
    quilometragem = models.CharField('Quilometragem', max_length=7)
    estado = models.CharField('Estado', max_length=10, choices=ICONE_CHOICES)
    preco = models.CharField('Preço', max_length=7)

    # OBS: Esses itens necessitam de valores default pois foram adicionados ao banco
    # depois do primeiro makemigrations, sendo assim, no primeiro makemigrations esses
    # dados não existiam. Após um novo makemigrations o banco de dados precisa de um default
    # para adicionar esses novos dados

    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={
        'thumbnail': {'width': 240, 'height': 240, 'crop': True}}, default='#')
    # default, necessário. Pois foi apresentado a seguinte mensagem
    # You are trying to add a non-nullable field 'imagem' to carro without a default.

    motor = models.CharField('Motorização', max_length=3, default='#')
    # default, You are trying to add a non-nullable field 'motor' to carro without a default

    cambio = models.CharField('Câmbio', max_length=15, choices=ICONE_CHOICES2, default='#')

    class Meta:
        verbose_name = 'Carros'
        verbose_name_plural = 'CARROS'

    def __str__(self):
        return self.modelo
    # Retorna o nome do modelo na página admin em 'Recent Actions' - 'My actions'