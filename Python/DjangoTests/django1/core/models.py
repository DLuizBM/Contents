from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço:', decimal_places=2, max_digits=10)
    estoque = models.IntegerField('Quantidade em estoque:')

    def __str__(self): # a função str apresenta o nome instanciado do objeto criadoProduto
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=15)
    email = models.EmailField('E-mail', max_length=20)

