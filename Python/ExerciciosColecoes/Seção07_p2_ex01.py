from random import randint

# Criando a matriz

mat = [[], [], [], []]

for l in range(0, 4):
    for c in range(0, 4):
        num = randint(1, 100)   # Gerando número aleatórios de 1 a 100
        print(f'Elemento ({l+1},{c+1}): {num}')
        mat[l].append(num)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'{mat[l][c]} ', end='')
    print('')

cont = 0
lista = []

# Procurando número maiores que 10

for l in range(0, 4):
    for c in range(0, 4):
        if mat[l][c] > 10:
            lista.append(mat[l][c])

# Mostrando a quantidade de número maiores que 10 e mostrando-os de forma organizada
print(len(lista))
lista.sort()
print(lista)

