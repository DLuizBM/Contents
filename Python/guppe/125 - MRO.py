"""
POO - MRO (Method resolution order)
MRO -> é a ordem de exeução dos métodos, quem será executado primeiro

Em python é possível conferir a ordem de execução dos métodos (MRO) de 3 formas:
    -via propriedade da classe__mro__
    -via métdod mro()
    -via help
"""


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

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrreste(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):

        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Aquatico, Terrreste):
    def __init__(self, nome):
        super().__init__(nome)

    def __mro_entries__(self, bases):   # Método para retornar o mro, bases é a classe ao qual quero informação
        return bases.__mro__            # bases.__mro__, retorna a informação do mro da classe

# Qual método cumprimentar() a classe Pinguim vai executar?
# Para enteder deve-se ter conhecimento do Method Resolution Order (MRO)
pinguim = Pinguim('Happy Feet')

# Para
# class Pinguim(Terrreste, Aquatico):
#     def __init__(self, nome):
#         super().__init__(nome)
# print(pinguim.cumprimentar())
# Saída: Eu sou Happy Feet da terra!
# print(Pinguim.__mro)
# (<class '__main__.Pinguim'>, <class '__main__.Terrreste'>, <class '__main__.Aquatico'>, <class '__main__.Animal'>, <class 'object'>)
# Prioridade para a classe Terrestre executar o método cumprimentar()

print(pinguim.cumprimentar())
# Saída: Eu sou Happy Feet do mar!


# ACESSO AO MRO VIA CLASSE
print(Pinguim.__mro__)
# (<class '__main__.Pinguim'>, <class '__main__.Aquatico'>, <class '__main__.Terrreste'>, <class '__main__.Animal'>, <class 'object'>)
# Primeiro são executados os métodos da classe Pinguim, caso não haja métodos, executa da classe Aquatico
# caso não haja, executa da classe Terreste, caso não haja da classe Animal e assim por diante
# Como o método cumprimentar() está presente nas classe Aquatico, Terrestre e Animal, há uma prioridade
# para executar o método da classe Aquatico, pois ela vem antes das outras 2

# ACESSO VIA MÉTODO
print(pinguim.__mro_entries__(Pinguim))
# (<class '__main__.Pinguim'>, <class '__main__.Aquatico'>, <class '__main__.Terrreste'>, <class '__main__.Animal'>, <class 'object'>)

# ACESSO VIA HELP
print(help(Pinguim))

