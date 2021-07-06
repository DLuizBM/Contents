# Criando a matriz

from random import randint

mat = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]

for l in range(0, 5):
    for c in range(0, 5):
        if l == c:
            mat[l][c] = 1
        else:
            mat[l][c] = 0

for l in range(0, 5):
    for c in range(0, 5):
        print(f'{mat[l][c]} ', end='')
    print('')
