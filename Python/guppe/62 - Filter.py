"""
FILTER
- Serve para filtrar dados de uma determinada coleção
- Em filter o tipo é objeto
- OBS: Os dados só são utilizados uma vez, como na função map
- Sempre retorna true ou false (é preciso, por exemplo manipular para mostrar os valores), é
o valor booleano que decide se o valor entra ou não, numa lista por exemplo. Map retorna valores
# Exemplos

# Biblioteca statistics

import statistics

dados = [1.1, 2.8, 3, 3.5, 4.5, 6.2]

# médio com a função mean()

media = statistics.mean(dados)
print(f'A média é: {media}')
# OBS: Assim como a função map(), filter() recebe dois parâmetros
# sendo função e iterável

res = filter(lambda x: x > media, dados)
print(list(res))

# Dados faltantes

paises = ['', 'Brasil', '', 'Argentina', '', 'Uruguai']

res = filter(None, paises)
print(list(res))
# Tipo None, quando passado desse forma exclui os dados vazios
res = filter(lambda pais: pais != '', paises)
res = filter(lambda pais: len(pais) > 0, paises)

# Por list comprehension
paises = ['', 'Brasil', '', 'Argentina', '', 'Uruguai']
print([pais for pais in paises if pais != ''])

# Exemplo
# Lista de dicionários com listas dentro, filtrar quem ganhou títulos

pilotos = [
    {'piloto': 'Fernando Alonso', 'Títulos': ['Ganhei 2 titulos', '2005 e 2006']},
    {'piloto': 'Mark Webber', 'Títulos': []},
    {'piloto': 'Ayrton Senna', 'Títulos': ['Ganhei 3', '89, 90 e 91']},
    {'piloto': 'Rubinho', 'Títulos': []}
]

res = filter(lambda piloto: piloto['Títulos'], pilotos)
# função lambda pra fazer a verificação de cada dicionário da lista
# vai passar o dicionário 'piloto' pra 'res', se a chave 'Títulos', do dicionário,
# possuir algum valor.
print(list(res))
# dic = {'Dívida': []} UMA LISTA VAZIA TRANSFORMADA EM BOOLEAN É FALSO
# if dic['Dívida']: para teste se há alguma coisa naquela chave daquele dicionário
    # print(dic)    basta usar if dicionário[chave], se houver alguma coisa, retorna true

# E quem não ganhou?
res = filter(lambda piloto: not piloto['Títulos'], pilotos)
print(list(res))


"""

# Combinando filter() com map()
# Devemos criar uma lista contento, sua instrutora é + nome, desde que cada nome
# tenha menos de 5 caracteres

nomes = ['vanessa', 'ana', 'maria']

# res = map(lambda nome: len(nome) < 5, nomes)
# print(list(res))
# Fazendo comparações como a da expressão acima, o map() devolve valores booleanos
# Saída = [False, True, False]
# res = filter(lambda nome: len(nome) < 5, nomes)
# print(list(res))
# Saída = ['ana']
# Já o filter em comparações devolve o valor presente na variável

# Por isso que na expressão a seguir o map vem antes do filter, não usar map quando
# tiver comparação e estrutura de controle, a não ser que seja desejado o valor booleano

res = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(res)

numbers = list(range(0, 100))
pair = (lambda number: number % 2 == 0)
which_pair = list(filter(pair, numbers))
print(which_pair)