from random import randint


def soma_coluna(coluna, *args):
    """
    Função que soma a coluna de uma matriz
    :param coluna:
    :param args:

    """
    tot = 0
    for l in range(0, len(args)):
        tot = tot + args[l][coluna - 1]
    print(tot)


mat = [[], [], [], [], [], [], []]

for l in range(0, 7):
    for c in range(0, 6):
         num = randint(10, 99)
         mat[l].append(num)

for l in range(0, 7):
    for c in range(0, 6):
        print(f'{mat[l][c]} ', end='')
    print('')

col = int(input("Digite a coluna que você somar: "))
while col <= 0 or col > 6:
    col = int(input("Digite a coluna que você somar: "))

soma_coluna(col, *mat)