"""
Métodos -> São funções dentro de classes. Representam os comportamentos dos objetos, as ações que esses
podem realizar no sistema.
Métodos são escritos em letras minúsculas, se for composto será separado por underline
ex: def nome_completo():

Em python dividimos os métodos em 2 grupos:
- De instância
    __init__ é chamado de método construtor, sua função é construir o objeto a partir da classe
    Os métodos dunder (double underline) são chamados de métodos mágicos
    São chamados de métodos de instância, pois é necessário uma instância da classe para utilizá-lo

- De classe: Não estão vinculados a nenhuma instância de classe, mas sim diretamente a ela
    É utilizado um decorator para indicar que o método é de classe e não de instância
    Método de classe não tem acesso a atributos de instância
    Métodos de classe em python são conhecidos como métodos estáticos
    É ideal usar método de classe quando não se faz acesso a nenhum atributo da classe, se fizer acesso aos atributos
    da classe, então deve-se usar métodos de instância

# Métodos de instância

class Produto:
    contador = 0

    def __init__(self, nome, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        return self.__valor - self.__valor * porcentagem


p1 = Produto('Xbox One', 2500)
print(p1.desconto(0.15))    # 2125.0
# Acessando o método desconto e mostrando o valor com desconto
# Notar que só é possível acessar o método desconto após criar o objeto e passar o valor dos atributos
# pois o método desconto precisa do valor de um dos atributos (valor) para poder ser executado, por isso é chamado
# método de instância. Pois é necessário instanciar um objeto para usá-lo
print(Produto.desconto(p1, 0.15))   # 2125.0
# Outra forma de trabalhar com métodos de instância, passando objeto em si(p1, no caso o self) e o desconto


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.encrypt(senha, rounds=200000, salt_size=16)

    def nome_completo(self):    # não é necessário colocar nome e sobrenome após o self,
        return f'{self.__nome} {self.__sobrenome}'  # pois como esse método está dentro da classe ele herda tudo nela

    # def __correr__(self, metros):   # Não é recomendado para desenvolvedores criar métodos dunder, mas é possível
        # print(f'{self.__nome} está correndo {metros} metros.')

    def pega_senha(self):
        return self.__senha


user1 = Usuario('Lewis', 'Hamilton', 'hamilton@gmail.com', '1234')
user2 = Usuario('Ayrton', 'Senna', 'senna@gmail.com', '2345')
print(user1.nome_completo())
print(user2.nome_completo())
print(Usuario.nome_completo(user1))
# Passando o self (user1) para a classe, dessa forma ela sabe qual o objeto e executa

print(user1.pega_senha())
# print(user1._Usuario__senha) possível, porém incorreto
# o ideal é que as senhas fossem criptografadas. Para isso, basta instalar a biblioteca passlib
# pip install passlib


from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        # rounds -> faz 200K embaralhamentos para gerar a senha
        # salt_size -> tamanho do texto que será juntado a senha para criptografar

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def pega_senha(self):
        return self.__senha

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):    # se senha é igual a self.__senha retorna true
            return True
        return False


nome = input('Qual seu nome? ')
sobrenome = input('Qual seu sobrenome? ')
email = input('Qual o seu email? ')
senha = input('Qual a sua senha? ')
confirma_senha = input('Por favor, confirme a senha: ')

if senha == confirma_senha:
    user1 = Usuario(nome, sobrenome, email, senha)
else:
    print('OPS! O usuário não foi criado :( .')
    exit(1)

senha = input('Entre com a senha: ')

if user1.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado.')

print(f'Senha user criptografada: {user1.pega_senha()}')

##################################################################################

# Métodos de classe

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuário no sistema.')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def pega_senha(self):
        return self.__senha

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):    # se senha é igual a self.__senha retorna true
            return True
        return False


user = Usuario('Ayrtons', 'Senna', 'senna@gmail.com', '1234')
Usuario.conta_usuario() # forma correta de acessar método de classe
user.conta_usuario() # forma incorreta


# Métodos de instância


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):     # O método construtor constroi o objeto
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


# Métodos privados: São métodos que só são acessíveis dentro da classe
# para criar métodos privados deve-se começar com __metodo()

# Métodos estáticos: O python possui métodos de classe(que em outra linguagens são métodos estáticos)
# e métodos estáticos

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuário no sistema.')

    @staticmethod # não tem acesso a instância do objeto e nem a classe
    def codigo():
        return 'URX'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def pega_senha(self):
        return self.__senha

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):    # se senha é igual a self.__senha retorna true
            return True
        return False

    def __gera(self): # Método privado
        return self.__email.split('@')[0]
        # separando pelo @: ['nome', 'email.com]
        # pegando na posição [0]: nome
        # exemplo: ayrton@gmail.com
        # ['ayrton', 'gmail.com']


user = Usuario('Ayrtons', 'Senna', 'senna@gmail.com', '1234')
Usuario.conta_usuario() # forma correta de acessar método de classe
user.conta_usuario() # forma incorreta


# print(user.__gera()) apresentará, pois o objeto user não tem esse atributo

print(user._Usuario__gera())
# acessando com name mangling, não é correto fazer isso, embora seja possível

# Acessando o método estático
print(Usuario.codigo())

"""


class Person:

    bones = 200

    @classmethod
    def default_bones(cls):
        return cls.bones

    @staticmethod
    def default_eyes(eyes=2):
        return eyes
    # com self é possível ter acesso aos atributos do objeto
    # com cls é possível ter acesso aos atributos da classe
    # o método estático não consegue utilizar nem self nem cls
    # por isso, ele não tem acesso aos atributos de classe e nem de instância

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_face(self):
        return f"{self.__name} has {Person.default_eyes()} blue eyes" \
               f" and {self.__get_hair()} hair"

    @staticmethod
    def __get_hair():
        return "blonde"


person = Person("Naruto")
print(Person.default_bones())
print(person.default_eyes())  # o objeto consegue acessar o método estático
print(person.get_face())
