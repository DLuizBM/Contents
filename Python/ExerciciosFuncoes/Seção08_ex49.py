from random import randint

def soma_acima_diagonal(*args):
    """
    Função que soma os elementos abaixo da diagonal principal
    :param args:
    :return:
    """
    lista = []
    for l in range(0, 5):
        for c in range(0, l):
            lista.append(args[l][c])
    print(lista)
    print(sum(lista))


mat = [[], [], [], [], []]

for l in range(0, 5):
    for c in range(0, 5):
        num = randint(0, 20)
        mat[l].append(num)

for l in range(0, 5):
    for c in range(0, 5):
        print(f'{mat[l][c]} ', end='')
    print('')

soma_acima_diagonal(*mat)
