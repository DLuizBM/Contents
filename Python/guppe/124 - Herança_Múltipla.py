"""
POO - Herança Múltipla

Herança múltipla é a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas
as classes herdadas.

OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por multiderivação direta;
    - Por multiderivação indireta;



# Exemplo 1 - Multiderivação Direta

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Multiderivacao(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiderivacao(Base3):
    pass


OBS: Não importa se a derivação é direta ou indireta, a classe que fizer a herança, herdará
todos os atributos e métodos das super classes
"""

# Exemplo


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):  # Sobreescrevendo o método cumprimentar da super classe Animal
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrreste(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):     # Sobreescrevendo o método cumprimentar da super classe Animal
        #   print(super().cumprimentar())
        # Com esse print aparecerá 'Eu sou self.__nome do mar', apresentando a saída do método cumprimentar
        # da classe Aquatico
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrreste, Aquatico):# Realizando a herança múltipla.Se ordem de herança for alterada(Aquatico, terrestre)
    def __init__(self, nome):      # a saída em pinguim.cumprimentar(Eu sou Happy Feet da terra!), também será alterada
        super().__init__(nome)     # passando para (Eu sou Happy Fert do Mar!.


# Qual método cumprimentar() a classe Pinguim vai executar?
# Para enteder deve-se ter conhecimento do Method Resolution Order (MRO)

pinguim = Pinguim('Happy Feet')
print(pinguim.cumprimentar())
# Eu sou Happy Feet da terra!


# O objeto é instância de...
print(f'pinguim é instância de Terreste?{isinstance(pinguim, Terrreste)}')
print(f'pinguim é instância de Aquático?{isinstance(pinguim, Aquatico)}')
print(f'pinguim é instância de Animal?{isinstance(pinguim, Animal)}')
print(f'pinguim é instância de object?{isinstance(pinguim, object)}')   # Toda classe herda de object

