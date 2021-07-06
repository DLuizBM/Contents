"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

Objetos que podem possuir muitas formas/se comportar de formas diferentes

Quando reescrevemos um método, fazemos o overrindig. Overrinding é a melhor representação
de polimorfismo. Pois podemos em cada parte do código dar um comportamento diferente para
o mesmo método.
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha deve implementar o método.')

    def comer(self):
        print(f'{self.__nome} está comendo.')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):    # Sobreescrevendo o método falar da super classe
        return f'O {self._Animal__nome} está falando WAU WAU'


class Boi(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'O {self._Animal__nome} está falando MUUUU'

    # Dando comportamentos diferentes para o método falar, entendemos que ele pode ter várias formas
    # e que cada forma pode ser aplicada a um tipo de objeto. Isso é polimorfismo.

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def come_gato(self):
        return f'{self.comer()}'
    # chamando o método comer da super classe


c1 = Cachorro('Rex')
print(c1.falar())

g1 = Gato('Xanim')
g1.comer()  # comer é um método da super classe Animal, a Classe gato herda esse método
g1.come_gato()  # método come_gato() faz o mesmo do método comer() da super classe
g1.falar()  # Erro, pois o método não foi sobreescrito na classe gato

