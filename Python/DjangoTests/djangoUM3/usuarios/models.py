from django.db import models

# from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, BaseUserManager


"""
AbstractBaseUser não inclui algumas funcionalidades
BaseUserManager, gerenciador do usuário, vai ser necessário criar um gerenciador
para esse usuário que estamos criando

"""


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    # email, password e **extra_fields, passado pelo desenvolvedor, não vem da função
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório.')
        email = self.normalize_email(email) # ajusta o email para o formato correto, vem do BaseUserManager
        user = self.model(email=email, username=email, **extra_fields)
        print("Self models", self)
        print("Dir.models", dir(self))
        """
        criando um model do usuário, com email, username e **extra_fields
        onde email vai ser o próprio email e username vai ser email também, que vai ser usado pra logar
        
        """
        user.set_password(password) # criptografa a senha
        user.save(using=self._db)
        # salvando usando(using) o banco de dados (self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        # extra_fields.setdefault cria o campo is_superuser=False
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=true')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Staff precisa ter is_staff=true')

        return self._create_user(email, password, **extra_fields)

    """
    create_user e create_superuser executam a _create_user, ela sim cria o usuário
    O BaseUserManager não possui os métodos create_user e create_superuser, o UserManager sim
    dessa forma, devemos criar esses métodos manualmente. UserManager herda de BaseUserManager.
    O _create_user faz o processo de criação no banco de dados
    """


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    # campo que vai fazer acesso juntamente com a senha
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']
    # campos para fazer o cadastro do superuser
    def __str__(self):
        return self.email

    objects = UsuarioManager()
    # Os objetos desse model são gerenciados por UsuarioManager()
    # sem essa especificação, o gerenciador vai ser o padrão do django
    # e dessa forma, não funcionará a autenticação por email

