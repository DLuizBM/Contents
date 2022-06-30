from collections import namedtuple
from timeit import timeit

Pessoa = namedtuple('Pessoa', 'nome email')
# namedTuple é usado para criar classe de forma mais rápida
# IdentificadorDeInstancia = namedTuple(nomeDaClasse, atributos)
felicity = Pessoa('Felicity', 'felicity@gmail.com')
print(timeit('felicity.email', globals=globals()))
# globals, é onde ele vai fazer a busca de informações
# globals(), é o contexto que estamos trabalhando
# A busca em python 3.8 é mais rápida que em python 3.7, por exemplo

import sys
print(sys.getsizeof(list(range(15092021))))
# buscando a quantidade de bytes necessário para gerar uma lista desse tamanho
# em python 3.8, o gerenciamento de memória também foi melhorado