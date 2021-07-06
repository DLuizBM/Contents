from django.db import models
from stdimage.models import StdImageField
import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criacao = models.DateField(verbose_name=None, name='Criação', auto_now_add=False)
    modificacao = models.DateField('Data de atualização', auto_now=True)
    tem_estoque = models.BooleanField('Tem em Estoque?', default=True)

    class Meta:
        abstract = True


class Carro(Base):
    ICONE_CHOICES = (
        ('Novo', 'Novo'),
        ('Usado', 'Usado'),
    )
    nome = models.CharField('Nome do Veículo', max_length=30)
    marcas = models.TextField('Marca', max_length=15)
    ano = models.CharField('Ano de Fabricação', max_length=4)
    modelo = models.CharField('Ano do Modelo', max_length=5)
    motorizacao = models.CharField('Motorização', max_length=10)
    quilometragem = models.CharField('Quilometragem', max_length=6)
    preco = models.CharField('Preço', max_length=10)
    estado = models.CharField('Estado', max_length=20, choices=ICONE_CHOICES)
    # imagens = StdImageField('Imagem', upload_to='', variations={'thumb': (240, 240)})
    # imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 360, 'length': 360, 'height': 360, 'crop': True}})
    imagem = StdImageField(upload_to=get_file_path, variations={
        'thumbnail': {"width": 100, "height": 100, "crop": True}
    })

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'CARROS'

