"""
Ranges: são utilizados para gerar sequências de números não
aletórias, mas sim, especificadas.

Formas gerais:

1-range(valor_de_parada)

Obs: valor_de_parada não inclusivo com início padrão 0 e passo de 1 em 1

for num in range(11):
    print(num)

2-range(valor_de_início(inicio especificado pelo usuário), valor_de_parada)

for num in range(2, 5):
    print(num)

3-range(valor_de_inicio(inicio especificado pelo usuário), valor_de_parada, passo(especificado pelo usuário))

for num in range(1, 11, 2):
    print(num)

4-range(valor_final, valor_de_parada, passo)
"""
for num in range(10, 0, -1):
    print(num)

