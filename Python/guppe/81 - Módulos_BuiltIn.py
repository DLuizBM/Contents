"""
Módulos built in - módulos integrados que vem com o python

# utilizando alias(apelidos) para chamar módulo

import random as rdm
print(rdm.random())
# rdm vai ser o apelido para chamar o módulo random

# Podemos importar todas as funções de um módulo utilizando o *

from random import *
print(random())
# dessa forma basta conhecer o nome da função para fazer a chamada


# utilizando alias(apelidos) para chamar função

from random import randint as rdi
print(rdi(1, 10))

from random import randint as rdi, random as rdm
print(rdm())

"""

# Quando se usam muitas funções de um módulo, costuma-se usar tuple para deixar mais organizado
from random import (
    random,
    randint,
    uniform,
    shuffle
)
print(random())
print(randint(1, 3))
print(uniform(1, 5))
a = [1, 2, 3, 4]
shuffle(a)
# para shuffle deve ser passado uma lista
print(a)
