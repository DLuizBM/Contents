"""
Ex: 

def function(texto: str) -> str:
    pass

As annotations servem para especificar um tipo. Na função acima
str está anotando que texto é do tipo string.


import math

def circunferecia(raio: float) -> float:
    return 2 * math.pi * raio

print(circunferecia.__annotations__)
# annotations devolve um dicionário com as annotations em um função, por exenplo
# {'raio': <class 'float'>, 'return': <class 'float'>}


# Declaração de variável 

text: str = "Hello world"
raio: float = 60.05
check: bool = True

print(__annotations__)
# mostra todos os annotations presentes

"""

class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.idade: int = idade
        self.__peso: float = peso
    
    def andar(self) -> str:
        return f"{self.__nome} está andando"

    @property
    def name(self) -> str:
        return self.__nome

    @name.setter
    def name(self, name: str) -> None:
        self.__nome = name


pessoa: Pessoa = Pessoa(nome="Messi", idade=35, peso=70.25)
print(pessoa.andar())
# print(p.__annotations__)  a instância não tem annotations
print(pessoa.andar.__annotations__) # a função possui annotations
