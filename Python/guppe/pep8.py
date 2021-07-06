"""
PEP 8- Pyhthon Enhancement Proposal

São prospostas de melhoria para a linguagem python

A ideia é que possamos escrever códigos em Python de forma Pythônica

[1] - Utilize Camel Case para nomes de classes;



class Calculadora:
    pass


class CalculadoraCientifica:
    pass




[2] - Utiliza nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_impar():
    pass


numero = 4;

[3] - Utilize 4 espaços para identação (NÃO USAR TAB)


if 'a' in 'banana':
    print('tem')

[4] -  Linhas em branco
- Separar funções e definições de classe com 2 linhas em branco
- Métodos dentro de uma classe devem ser separados com 1 linha em branco


[5] - imports


- Imports devem sempre ser feitos em linhas separasa;

#Import errado

import sys, os

#Import certo

import sys
import os

#Não há problemas em utilizar

from types import StringTypes, ListTypes

#Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
   StringTypes,
   ListTypes,
   OutroTypes,
)

#imports devem ser colocados no topo de arquivos, logo depois de comentários ou docstring
#e antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções

# Não faça:

função(_algo_[_1_], {_outro: 2_}_)

# Faça:

função(algo[1], {outro: 2})

# Não faça:

algo_(1)

# Faça:

algo(1)

# Não faça:

dict_['chave'] = lista_[indice]

# Faça;

dict['chave'] = lista[indice]

# Não faça:

x______________= 1
y______________= 2
variavel_longa = 3

# Faça:

x = 1
y= 2
variavel_longa = 3

[7] - Termine sempre uma instrução com uma nova linha

"""
