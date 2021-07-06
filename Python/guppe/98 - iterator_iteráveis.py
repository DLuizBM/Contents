
"""
Iterator e iterable(iterável)

Iterator:
- Um objeto que pode ser iterado
- Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada

Iterable:
- Um objeto que irá retornar um iterator quando a função iter() for chamada

"""

nome = 'Flamengo'    # A string é um iterável, mas não um iterator
lista = [1, 2, 3, 4, 5, 6]  # a lista de números é um iterável, mas não um iterator


it = iter(nome) # transformando nome em iterator
print(next(it)) # retorno da função next()
print(next(it))

it2 = iter(lista)
print(next(it2))
print(next(it2))




