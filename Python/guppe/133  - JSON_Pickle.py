"""
JSON e Pickle
Java Script Object Notation


import json

ret = json.dumps(['produto', {'playstation 4': ('2TB', 'Novo')}])
print(ret)


import json


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-lata')
print(felix.__dict__)
ret = json.dumps(felix.__dict__)
print(ret)


# JSON com Pickle: pip instal jsonpickle

import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-lata')
ret = jsonpickle.encode(felix)
print(ret)



# Escrevendo o arquivo JSON Pickle

import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-lata')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)


import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)

# a classe deve estar junto do processo de decodificação
# se não, é apresentado erro
"""
import json

lst = ['dica', 'ja']
context = {'words': lst}
ret = json.dumps(context)
print(ret)