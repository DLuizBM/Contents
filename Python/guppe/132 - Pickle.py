"""
Pickle

A função do pickle é realizar o seguinte processo:

Objeto Python -> Binarização
Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

#OBS: o módulo Pickle não é seguro contra dados maliciosos e desta forma
não é recomendado trabalhar com arquivos pickle vindos de fontes desconhecidas

"""

import pickle


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} está comendo!!')

    @property
    def nome(self):
        return self.__nome


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self._Animal__nome} está miando!!')
        # para usar self.nome, basta declarar a propriedade(@property) no método nome na classe animal


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo!!')
        # com a propriedade (@property) definida


felix = Gato('Felix')
pluto = Cachorro('Pluto')

print(felix.nome)
print(pluto.nome)

# Fazendo a escrita em arquivo pickle
# with open('animais.pickle', 'wb') as arquivo:
    # wb, escreve em binário
#    pickle.dump((felix, pluto), arquivo)


# Fazendo a leitura

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    # load carrega os objetos python em 'gato' e 'cachorro'
    # assim sendo, 'gato' e 'cachorro' se tornam objeto com os métodos e atributos
    # definidos na classe
    print(f'O gato chama-se: {gato.nome}')  # com @property
    print(f'O cachorro chama-se: {cachorro._Animal__nome}') # sem @property no método nome
    gato.mia()
    cachorro.late()