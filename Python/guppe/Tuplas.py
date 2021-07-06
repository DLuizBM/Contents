# coding=utf-8
"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas
Existem basicamente duas diferenças:

1- Tuplas são representadas por parênteses ()
2- Tuplas são imutáveis: Isso significa que ao se criar um tupla ela não muda.
Todas operação em uma tupla gera uma nova tupla.


# CUIDADO 1: As tuplas são representadas por parênteses, mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento
tupla3 = (4)    # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,)   # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4,   # Isso é uma tupla
print(tupla5)
print(type(tupla5))
# Podemos concluir que tuplas são definidas pela vírgula e não pelo parênteses

# Podemos gerar um tupla dinâmicamente com range/ Possível trabalhar com os parâmentros do range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Decomposição de tuplas

tupla = ('Carro', 'Moto')

v1, v2 = tupla

print(v1)
print(v2)

# Métodos para fazer adição e remoção de elementos em tuplas não existem, dado o fato de tuplas serem imutáveis


# Soma, valores máximo, mínimo e tamanho

# Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print(tupla1)
print(tupla2)

print(tupla1 + tupla2)


# Verificando se determinado está na tuplas

tupla1 = 'carro'

a = tuple(tupla1) # Como usar o comando tuple

print(a)

print('c' in tupla1) # verificando se 'c' está na tupla1

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'a', 'b')

print(tupla.count('a'))

escola = tuple('Geek university') # tupla converte string pra tupla

print(escola.count('e'))

# Devemos utilizar tuplas sempre que não precisamos mudar os dados em uma coleção

# Exemplo 1

meses = ('janeiro', 'Fevereiro', 'Março', '...')
# Meses do ano não precisam ser modificados, pois não há meses para serem inseridos ou retirados
print(meses)

# O acesso de elementos numa tupla também é semelhante ao feito em uma lista

print(meses[2])

# Iterando com While

a = len(meses)
i = 0
while i < a:
    print(meses[i])
    i = i + 1

# Verificando o posição que cada elemento se encontra na tupla
meses = ('janeiro', 'Fevereiro', 'Março', '...')
print(meses.index('Março'))
print(meses.index('...', 2)) # Proxurando a partir do índice 2
# Caso o elemento não exista, será apresentado erro ValueError

# Slicing
# tupla[início:fim:passo]

print(meses[0::])
print(meses[0::2])
print(meses[0:2:])

# Por que utilizar tuplas?
# Tuplas são mais rápidas pelo fato de serem imutáveis
# Deixam o código mais seguro, isso porque elementos imutáveis trazem segurança para o código


"""

# Copiando tuplas

tupla1 = (10, 11, 12, 13, 2, 5, 2)
print(tupla1)

nova = tupla1 # Na tupla não temos o problema de Shallow copy
print(nova)
print(tupla1)
print(tupla1.index(2, 3))
#procure o índice do elemento 2 a partir do índice 3


