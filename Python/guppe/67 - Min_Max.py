"""
MIN E MAX

max() -> retorna o maior valor de um iterável ou o maior valor de 2 ou mais elementos

print(max(10, 450, 321, 43))
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c', 'g', 'h')) # quanto mais perto do fim do alfabeto, maior a letra

min() -> retorna o menor valor de um iterável ou o menor valor de 2 ou mais elementos

print(max(10, 450, 321, 43))
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c', 'g', 'h')) # quanto mais perto do início do alfabeto, menor a letra

"""

# Exemplos

nomes = ['Senna', 'Hamilton', 'Alonso', 'Prost']

print(max(nomes)) # Senna
print(min(nomes)) # Alonso
# max e min levam em consideração a letra de início e não o tamanho da string

# Modificando para pegar o tamanho da strings
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

musicas = [
    {'faixa': 'Asa Branca', 'tocou': 7},
    {'faixa': 'Espumas ao vento', 'tocou': 3},
    {'faixa': 'Juazeiro Petrolina', 'tocou': 4}
]

# print(max(musicas, key=lambda musica: musica['tocou']))
# print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio! Imprimir o título da música mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['faixa'])
# do obejto (lembrar de JS, dicionário em JS é obejto), quero só a chave, é o que é feito na solução abaixo
b = min(musicas, key=lambda musica: musica['tocou'])
# o que é passado para b é o dicionário que tem a chave tocou com menor valor.
# ou seja, dicionários foram organizados na ordem crescente de acordo com o número de vezes
# que a música foi tocada.O mesmo serve para o max acima.
print(b)

lista = []
for musica in musicas:
    lista.append(musica['tocou'])
print(lista)
for i in range(0, len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

max = lista[2]
mais =[]
for musica in musicas:
    if musica['tocou'] == max:
        mais.append(musica['faixa'])
print(mais)


