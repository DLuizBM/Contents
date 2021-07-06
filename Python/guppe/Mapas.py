# coding=utf-8
"""
Mapas em python são conhecidos como dicionários


receita = {'jan': 100, 'fev': 200, 'marc': 300}

print(receita)

# Iterando sobre dicionários
for chave in receita:
    print(chave)    # imprime a chave correspondente (jan, fev, marc)

for chave in receita:
    print(receita[chave])   # imprime o valor corresponde para cada chave (100, 200, 300)

for chave in receita:
    print(f'{chave}:{receita[chave]}.')

# Acessando as chaves
print(receita.keys())   # Cria um dicionário de chaves

for chave in receita.keys():    # Método pythônico de indicar que está trabalhando com chaves
    print(receita[chave])


# Acessando os valores
print(receita.values())     # Cria um dicionário de valores

for valor in receita.values():  # Método pythônico de especificar que está trabalhando com os valores do dicionário
    print(valor)

# Desempacotando dicionários
print(receita.items())  # Gera um lista de tuplas contendo a chave e o valor
for chave, valor in receita.items():
    print(f'Chave:{chave} / Valor:{valor}')
"""

receita = {'jan': 100, 'fev': 200, 'mar': 300}

print(receita)

# Soma, Valor máximo, valor mínimo, Tamanho
# Se o valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))


