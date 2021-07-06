from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals
# faz com seja possível aplicar sinais antes e depois de inserir dados no banco de dados
from django.template.defaultfilters import slugify
# slug é colocar o título de uma determinada págima pra ser uma url válida


class Base(models.Model): # models.Model, significa que essa classe extende models.model
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
    # uma classe abstract não é criada em banco de dados (a classe Base é abstrata)
    # serve somente de rascunho para outras classes


class Produto(Base):    # a classe produto já vai ter os atributos da classe base
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    # upload_to -> será criado um diretório produtos com as imagens
    # thumb cria uma variação da imagem com o tamanho especificado
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)
    # slugify, funcionamento
    # Maria Mole
    # maria-mole


signals.pre_save.connect(produto_pre_save, sender=Produto)
# essa linha será executada, se o Produto for salvo, será enviado um sinal para executar a função produto_pre_save
# isso antes de ser salvo. Executando a função ele vai instanciar slug e colocar nele o nome do produto
# transformando todas as letras em minúsculo e colocando '-' entre espaços
