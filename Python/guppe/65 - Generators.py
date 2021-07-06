"""
GENERATORS

São tuples comprehensions, dá-se o nome de generators
Generator é mais performático, exige menos recurso da memória

nome = ['carla', 'cristina', 'camila', 'julia']

# List comprehension

res = [n for n in nome if n[0] == 'c']
print(res)
# Saída -> ['carla', 'cristina', 'camila']

res = [n[0] == 'c'for n in nome]
print(res)
# Saída -> [True, True, True, False]

# Generator

res = (n[0] == 'c'for n in nome)
print(tuple(res))
# Saída -> [True, True, True, False]
print(any((n[0] == 'c'for n in nome)))

from sys import getsizeof
# Essa função devolve o tamanho do elemento em bytes

print(getsizeof('Geek'))
print(getsizeof(9))

from sys import getsizeof

# Gerando lista de números com list comprehension

lis = getsizeof([num * 10 for num in range(1, 1000)])

# Gerando lista de números com set comprehension

Set = getsizeof({num * 10 for num in range(1, 1000)})

# Gerando lista de números com dictionary comprehension

dic = getsizeof({chave: chave * 10 for chave in range(1, 1000)})

# Gerando lista de números com generators

gen = getsizeof((num * 10 for num in range(1, 100000)))

print(f'Lista Comprehension: {lis}')
print(f'Set Comprehension: {Set}')
print(f'Dic Comprehension: {dic}')
print(f'Generator: {gen}')

"""
# É possível iterar no generator?

from sys import getsizeof

gen = (num * 10 for num in range(1, 100000))
lista = []

for num in gen:
    print(num)
    lista.append(getsizeof(num))

print(sum(lista))
