# coding=utf-8
"""
Módulo collections

Named tuple: São tuplas diferenciadas, onde, especificamos um nome para a mesma e também
parâmetros


"""
from collections import namedtuple

# Precisamos definir o nome e o parâmetro

# Forma 1 - Declaração Named tuple

# cachorro = namedtuple('cachorro',  'idade raca nome')

# Forma 2 - Declaração Named tuple

# cachorro = namedtuple('cachorro',  'idade, raca, nome')

# Forma 3 - Declaração Named tuple

ca = namedtuple('cachorro',  ['idade', 'raca', 'nome'])
print(ca)
# o Nome da tupla é cachorro
# e ela contém 3 variáveis(idade, raça e nome)

# Usando a named tuple

raca = 'pitbul'
nome = input()

tompero = ca(idade=2, raca=raca, nome=nome)
print(tompero)

# Acessando os elementos

# Forma 1
print(tompero[0])
print(tompero[1])
print(tompero[2])

# Forma 2
for cachorro in tompero:
    print(cachorro)

# Forma 3
print(tompero.idade)
print(tompero.raca)
print(tompero.nome)

montega = ca(idade=5, raca='fila', nome='montega')
print(montega)

# tupla carro
automovel = namedtuple('carro', ['motor', 'modelo'])
corolla = automovel(motor='1.8', modelo='2011')
print(corolla)