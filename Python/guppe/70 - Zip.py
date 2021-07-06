"""
ZIP
zip() -> Cria um iterável.(Zipe Object) que agrega  elemento de cada um dos iteráveis
passadas como entrada em pares.
- Se utilizado a primeira vez, some da memória
- Transforma os zipados em pares/trios/etc de tuplas
# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
zip2 = zip(lista2, lista1)
zip3 = zip(lista2, lista1)
zip4 = zip(lista2, lista1)

print(list(zip1)) #[(1, 4), (2, 5), (3, 6)]
print(tuple(zip2)) #((4, 1), (5, 2), (6, 3))
print(set(zip3)) #{(6, 3), (4, 1), (5, 2)}
print(dict(zip4)) #{4: 1, 5: 2, 6: 3}

lista3 = [6, 7, 8, 9, 10]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1)) #[(1, 4, 6), (2, 5, 7), (3, 6, 8)]
# OBS: O zip utiliza como parâmetro a menor lista como iterável
# se uma lista possui 2 elementos e outra 10, então só 2 elementos da segunda lista
# serão utilizados


# Diferentes iteráveis com zip

lista = [1, 2, 3]
string = ['a', 'b', 'c']
dic = {'a': 10, 'b': 20, 'c': 30}
zip1 = zip(lista, string)
print(list(zip1)) #[(1, 'a'), (2, 'b'), (3, 'c')]

zip2 = zip(dic, lista, string)
print(list(zip2)) # [('a', 1, 'a'), ('b', 2, 'b'), ('c', 3, 'c')]
zip3 = zip(dic.values(), lista, string)
print(list(zip3)) # [(10, 1, 'a'), (20, 2, 'b'), (30, 3, 'c')]


lista_de_tuplas = [(1, 2), (3, 4)]
print(list(zip(*lista_de_tuplas))) #[(1, 3), (2, 4)]
# * indica que está sendo descompactado

"""

pilotos = ['Senna', 'Hamilton', 'Prost']
titulo1 = [1988, 2008, 1985]
titulo2 = [1990, 2014, 1986]
titulo3 = [1991, 2015, 1989]

# Ano em que cada um ganhou o trimundial
tri = {ano[0]: max(ano[1], ano[2], ano[3]) for ano in zip(pilotos, titulo1, titulo2, titulo3)}
print(tri)

# Com map
trim = zip(pilotos, map(lambda ano: max(ano), zip(titulo1, titulo2, titulo3)))
print(dict(trim))
