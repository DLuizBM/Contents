# Criando a matriz

mat = [[], [], [], []]

for l in range(0, 4):
    for c in range(0, 4):
        a = l * c
        mat[l].append(a)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'{mat[l][c]} ', end='')
    print('')


