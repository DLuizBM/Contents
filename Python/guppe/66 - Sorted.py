"""
SORTED

- Não confundir com a função sort(), que só funciona com listas
- Sorted funciona com qualquer iterável, para que ele seja ordenado


# Exemplos

lista = [10, 9, 4, 5]

print(sorted(lista))
# Saída [4, 5, 9, 10] - sorted só organiza a lista e sempre devolve uma lista, independente do iterável
print(lista)
# Saída [10, 9, 4, 5] - a lista original permanece sem alteração
lista.sort()
print(lista)
# Saída [4, 5, 9, 10] - sort gera uma nova


numeros = (10, 9, 4, 5) # com tupla
print(sorted(numeros, reverse=True))
# ordena do maior para o menor


def chama(**kwargs):
    return f"{kwargs['piloto']} é um piloto"

# Mais complexos - ordenando uma lista de dicionário
# reverse no final é opcional, se colocado como true, ordenará na ordem inversa

pilotos = [
    {'piloto': 'Fernando Alonso', 'Títulos': ['Ganhei 2 títulos', '2005 e 2006']},
    {'piloto': 'Mark Webber', 'Títulos': []},
    {'piloto': 'Ayrton Senna', 'Títulos': ['Ganhei 3 títulos', '89, 90 e 91']},
    {'piloto': 'Rubinho', 'Títulos': ['2 vices']}
]
print(sorted(pilotos, key=lambda piloto: piloto['piloto'], reverse=True))
# Será passado cada piloto(cada dicionário) dentro da lista de pilotos
# para a função lambda, e a função lambda retornará o valor da chave piloto

# Se o dicionário tiver em uma lista a forma de trabalhar ele é assim:
# passa cada posição da lista(um dicionário), para uma variável e buscar a chave valor
# a = pilotos[0]
# for chave, valor in a.items():
#    print(f'{chave} {valor}')

# Ordenando pelo número de títulos
print(sorted(pilotos, key=lambda piloto: len(piloto['Títulos'])))

#for piloto in pilotos:
#    print(chama(**piloto))

"""
def chama(**kwargs):
    return f"{kwargs['tocou']}"

musicas = [
    {'faixa': 'Asa Branca', 'tocou': 7},
    {'faixa': 'Espumas ao vento', 'tocou': 3},
    {'faixa': 'Juazeiro Petrolina', 'tocou': 4}
]

print(sorted(musicas, key=lambda musica: musica['tocou']))
print(sorted(musicas, key=lambda musica: chama(**musica)))
# Lambda tem um papel fundamental para buscar cada elemento da coleção, sem lambda
# não é possível fazer esse tipo de interação em funções como sorted() e outras
# pois é ela que busca cada elementa da coleção, dentro de outra coleção. Por exemplo,
# só é possível buscar cada dicionário dentro da lista com o lambda. Se algo do tipo a seguir
# for feito:
# print(sorted(musicas, key=musica['tocou']))
# não será possível iterar sobre cada dicionário na lista, pois passando somente a chave,
# como demonstrado, não há como iterar.

pilotos = [
    {'piloto': 'Fernando Alonso', 'Títulos': ['Ganhei 2 títulos', '2005 e 2006']},
    {'piloto': 'Mark Webber', 'Títulos': []},
    {'piloto': 'Ayrton Senna', 'Títulos': ['Ganhei 3 títulos', '89, 90 e 91']},
    {'piloto': 'Rubinho', 'Títulos': ['2 vices']}
]
print(sorted(pilotos, key=lambda piloto: piloto['piloto'], reverse=False))
# Ordena em ordem alfabética
# pode-se ordenar também pelo tamanho da string len(piloto['piloto'])

