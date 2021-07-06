import uuid # gera valores hexadecimais diferentes, será usado para salvar cada imagem com um nome
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Data de criação', auto_now_add=True)
    # auto_now_add = adiciona automaticamente a data
    modificado = models.DateField('Atualização', auto_now=True)
    # auto_now = modifica automaticamente a data de atualizaçaõ do objeto
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servicos(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Camadas'),
        ('lni-mobile', 'Telefone'),
        ('lni-rocket', 'Foguete')
      # no banco de dados lni- é que vai ficar salvo no banco de dados
    ) # essa estrutura vai fazer uma caixa para selecionar o ícone desejado

    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=12, choices=ICONE_CHOICES)
    # Itens que serão registrados

    class Meta:
        verbose_name = 'SERVIÇOSS' # nome que fica no navegador para identificar a página e em outras partes,
        # como no fim dos serviços cadastrados
        verbose_name_plural = 'SERVICES' # nome em que deve ser clicado para fazer o registro dos serviços

    def __str__(self):   # apresenta o objeto
        return self.icone
    # saída: <bound method QuerySet.all of <QuerySet [<Servicos: lni-stats-up>, <Servicos: lni-cog>]>>
    # saída somente no terminal para saber uma informação do objeto, no caso está mostrando que a classe
    # Servico está com os icones lni-stats-up e lni-cog
    # sem o __str__
    # <bound method QuerySet.all of <QuerySet [<Servicos: Servicos object (1)>, <Servicos: Servicos object (2)>]>>
    # ou seja, não informações sobre o que está sendo utilizado na classe, apenas object(1), object(2)...
    # poderia mudar para return self.servico e assim teríamos o nomes dos serviçoes presentes na classe


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=30)

    class Meta:
        verbose_name = 'CARGO'
        verbose_name_plural = 'CARGOS'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=30)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    # ForeignKey -> herda o que está em care.Cargo, ou seja, vai herdar todos os cargos criados
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'length': 480, 'crop': True}})
    # upload_to -> mandando para get_file_path para criar o nome das imagens
    # StdImage vai criar um diretório com as imagens e colocar todas lá
    # crop = se necessário recortar, pode recortar
    facebook = models.CharField('Facebook', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'FUNCIONÁRIOS'

    def __str__(self):
        return self.nome


class Features(Base):
    ICONE_CHOICES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Laptop'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folhas'),
        ('lni-layers', 'Camadas'),
    )
    caracteristica = models.CharField('Feature', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Features'
        verbose_name_plural = 'CARACTERÍSTICAS'

    def __str__(self):
        return self.caracteristica





