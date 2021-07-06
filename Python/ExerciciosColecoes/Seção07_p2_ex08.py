from random import randint

mat = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        num = randint(1, 10)
        mat[l].append(num)

soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        # Somando os elementos acima da diagonal principal
        if l == c:
            for coluna in range(c+1, 3): # Vai somar os elementos de cada linha passando em cada coluna
                soma = soma + mat[l][coluna]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'{mat[l][c]} ', end='')
    print('')

print(soma)