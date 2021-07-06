from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.conf import settings
# a função get_user_model, permite que seja pego a configuração estabelecida
# se no settings fizermos a configuração AUTH_USER_MODEL, ele vai retornar a configuração
# estabelecida, se não, busca o User padrão do django
"""
# Forma 1 - Essa forma não permite customização


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    tittle = models.CharField('Tittle', max_length=200)
    text = models.TextField('Text', max_length=400)

    def __str__(self):
        return self.tittle



# Forma 2 - Usuário customizado


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete=models.CASCADE)
    tittle = models.CharField('Tittle', max_length=200)
    text = models.TextField('Text', max_length=400)

    def __str__(self):
        return self.tittle

"""
# Forma 3 - utilizando a função get para buscar de forma correta ou o usuário customizado ou o User


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name='Author', on_delete=models.CASCADE)
    tittle = models.CharField('Tittle', max_length=200)
    text = models.TextField('Text', max_length=400)

    def __str__(self):
        return self.tittle

# verificando o User utilizado
# no shell
# from django.contrib.auth import get_user_model
# get_user_model()
# <class 'django.contrib.auth.models.User'>
