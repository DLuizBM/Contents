# Import para gerar número aleatórios
import random

mat = [[], [], [], []]

for l in range(0, 4):
    for c in range(0, 4):
        # Gerando ponto flutuante com random, num intervalo de 1 a 100
        num = random.uniform(1, 100)
        mat[l].append(num)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'{mat[l][c]} ', end='')
    print('')

for l in range(0, 4):
    for c in range(0, 4):
        print(f'O elemento {mat[l][c]} está na posição: ({l+1},{c+1}).')