from random import randint

mat = [[], [], [], [], []]

for l in range(0, 5):
    for c in range(0, 5):
        num = randint(1, 99)
        while num in mat: # enquanto o número gerado já estiver dentro da matriz um
                          # novo número será gerado, até que seja diferente, para ser adicionado
            num = randint(1, 99)
        mat[l].append(num)

for l in range(0, 5):
    for c in range(0, 5):
        print(f'{mat[l][c]} ', end='')
    print('')