"""
Map
Com map fazemos o mapeamente de valores para função

import math

def area(raio):
    return math.pi * raio ** 2

raios = [1, 2, 3, 4]
areas = []
for r in raios:
    areas.append(area(r))
print(areas)
areas.clear()
# Fazendo a mesma função, mas com MAP
areas = map(area, raios)
# faça o mapeamento passando para a função area todos os raios
# recebe 2 parâmetros, o primeiro uma função o segundo um iterável
# retorna um objeto próprio do tipo MAP OBJECT
print(list(areas))
print(type(areas))

# Fazendo com lambda
print(list(areas)) # Dando um list(areas) de novo, ele zera, pois foi utilizado mais de uma vez, OBS abaixo explica
areas = map(lambda raio: math.pi * raio ** 2, raios)
print(list(areas))

# Com list comprehension
print(list(map(lambda raio: math.pi * raio ** 2, raios)))
# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera
# Lembrar de passar para um vetor os dados, caso seja necessário utilizar mais de uma vez no programa

# Map object retorna: f(x1), f(x2), f(x3), ... , f(xn)

"""

# Conversão

cidades = [('Brasília', 29), ('Juazeiro', 35), ('Petrolina', 37)]
# lembrando que, caso queira acessar o elemento dentro da lista
# deve-se passar 2 parâmetros: ex: Elemento 'Juazeiro' -> print(cidade[1][0])

celsius_f = lambda cidade: (cidade[0], (9/5) * cidade[1] + 32)
# Quando devolve 2 informações, deve-se ter os ()
# para essa função é passado um elemento da lista por vez ( uma tupla por vez) para a variável cidade
# ex: cidades[0] = ('Brasília', 29) -> a variável cidade então será uma tupla ('Brasília', 29)
# logo, cidade[0] = 'Brasília' e cidade[1] = '29'
print(list(map(celsius_f, cidades)))

