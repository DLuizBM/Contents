"""
Atributos
- Representam as características de um objeto

Em python, dividimos os atributos em 3 grupos
- Atributos de instância: São atributos declarados dentro do método construtor, podem ser públicos ou privados
    Por convenção ficou estabelecido que todo atributo é público
    Caso queiramos indicar que determinado atributo é privado, utiliza-se duplo undescor(__), antes de seu nome
    Isso é conhecido como Name Mangling.
    O que significa atributos de instância? Significa que ao criar instâncias/objeto de uma classe, todas as instâncias
    terão estes atributos.

- Atributos de classe(em algumas linguagens, atributos estáticos): São atributos declarados diretamente na classe, ou seja, fora do construtor, geralmente já inicializamos um valor
e este valor já é compartilhado entre todas as instâncias da classe(objetos), ou seja, ao invés de cada objeto ter seu valor do atributo,
como no caso de atributos de instância, com atributo de classe todos os objetos terão o mesmo valor

- Atributos dinâmicos: São atributos de instância que podem ser criados em tempo de execução. É exclusivo da instância(objeto) que o criou
São possíveis, mas não comum.



# Atributos de instância (Atributos públicos)
class Lampada:
    def __init__(self, voltagem, cor):  # __init__ -> este é o método construtor
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False
        # estes são os atributos de instância
        # self.__voltagem = voltagem
        # __ indica que os atributos são privados, logo só posso ter acesso a eles dentro da classe
        # devemos criar métodos para facilitar a utilização desses atributos


class ContaCorrente:
    def __init__(self, numero, limite, saldo): # __init__ métodos construtor
        self.numero = numero
        self.limite = limite
        self.saldo = saldo
        # self nada mais é do que o objeto que está executando o método
        # self.numero = numero -> o objeto ContaCorrente no atributo numero, vai receber numero

        # self não é obrigatório, pode-se usar outro nome, mas por convenção usa-se self
        # em JS/JAVA por exemplo usa-se this



minhaconta = ContaCorrente('123', '10000', '100')
# ContaCorrente() é o método __init__ sendo executado

# Atributos de instância (Atributos Privados)
# privados: só temos acesso dentro da classe em que foi declarado


class Usuario:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        # .nome é como vamos chamar no nosso sistema para ter acesso a variável nome
        # self.nome = telefone se chamarmos assim, vamos ter no atributo nome o valor de telefone
        self.__telefone = telefone
        self.__email = email
        # __(duplo underscore) indica que o atributo é privado

    def mostra_telefone(self):
        print(self.__telefone)

# Testando

user1 = Usuario('Hamilton', '555-555', 'hamilton@gmail.com')
print(user1.nome)
# Saída: Hamilton
#print(user.__telefone)
# Saída: AttributeError: 'Usuario' object has no attribute '__telefone'
print(user1._Usuario__telefone)
# Saída: 555-555. O python não impede de acessarmos um atributo privado, mas não é recomendado
# essa é uma forma de acessar um atributo privado (Name Mangling)
# a forma correta é criar outro método que faça acesso, como o método mostra_telefone

user1.mostra_telefone()

user2 = Usuario('Alonso', '777-777', 'alonso@gmail.com')
user3 = Usuario('Vettel', '999-999', 'vettel@gmail.com')

user2.mostra_telefone()  # 777-777
user3.mostra_telefone()  # 999-999
# A orientação consegue diferenciar os objetos e pegar as informações referente a cada um
###############################################################################################




# Atributos de classe


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


p1 = Produto('Xbox One', 'Vídeo Game', 2500)
p2 = Produto('Playstation 4', 'Video Game', 2450)
# Dess forma, cada atributo recebe um valor para si, todos são atributos de instância


class OutroProduto:
    imposto = 1.2

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * OutroProduto.imposto


p3 = OutroProduto('Xbox One', 'Vídeo Game', 2500)
p4 = OutroProduto('Playstation 4', 'Video Game', 2450)

print(p3.imposto)   # Acesso incorreto ao atributo de classe
print(p4.imposto)
# Saída: 1.2
# O mesmo valor para os dois, pois imposto é um atributo de classe e tem o mesmo valor para todos os objetos
# OBS: não é necessário criar uma instância de uma classe(objeto) para fazer acessa a um atributo de classe
# Basta apenas chamar a classe e o atributo.
print(OutroProduto.imposto)     # Acesso correto ao atributo de classe
print(p3.valor)
print(p4.valor)


class OutroProduto:
    imposto = 1.2
    contador = 0
    # imposto e contador são atributos de classe

    def __init__(self, nome, descricao, valor):
        self.id = OutroProduto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * OutroProduto.imposto
        OutroProduto.contador = self.id
        # self.id vai receber o valor de OutroProduto.contador + 1
        # OutroProduto.contador = self.id, ao final, OutroProduto.contador vai possuir o valor de self.id
        # e quando for executado de novo na primeira linha, OutroProduto.contador, vai estar atualizado
        # id é um atributo de instância, não é necessário que ele seja declarado no método construtor, pois ele utiliza
        # uma lógica diferente dos demais atributos


p1 = OutroProduto('Xbox One', 'Vídeo Game', 2500)
p2 = OutroProduto('Playstation 4', 'Video Game', 2450)

print(p1.id)    # 1
print(p2.id)    # 2
# Contador funcionou e cada produto agora tem seu id




class OutroProduto:
    imposto = 1.2
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = OutroProduto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * OutroProduto.imposto
        OutroProduto.contador = self.id


p1 = OutroProduto('Xbox One', 'Vídeo Game', 2500)
p2 = OutroProduto('Playstation 4', 'Video Game', 2450)

# criando o atributo dinâmico
p2.peso = '5Kg'     # Notar que na classe produto não tem o atributo peso
print(f'Produto:{p2.nome}\nDescrição:{p2.descricao}\nPreço:{p2.valor}\nPes:{p2.peso} ')
# print(f'Produto:{p1.nome}\nDescrição:{p1.descricao}\nPreço:{p1.valor}\nPes:{p1.peso} ')
# p1 não tem o atributo peso: AttributeError

print(OutroProduto.__dict__)
print(p1.__dict__)
print(p2.__dict__)
# acessando as informações da classe e dos produtos

# Deletando atributos de instância e dinâmicos
del p2.peso
print(p2.__dict__)
# será deletado o atributo peso
del p1.valor
print(p1.__dict__)
# será deletado o atributo valor
"""
from apt_pkg import Package


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person("Craque Neto", 54)

print(person.get_name())
print(person.__dict__)
#  {'_Person__name': 'Craque Neto', '_Person__age': 54}
print(dir(person))
