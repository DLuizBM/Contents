from random import randint

def verifica_matriz(*args):
    """
    Função verifica a quantidade de números maior que 10 que tem na matriz
    :param args:
    :return:
    """
    lista = []
    print('')
    for l in range(0, 4):
        for c in range(0, 4):
            if args[l][c] > 10:
                lista.append(args[l][c])
    print(len(lista))


mat = [[], [], [], []]

for l in range(0, 4):
    for c in range(0, 4):
        num = randint(1, 100)
        if num in mat:  # Gera números aleatórios, por linha, na matriz
            while num in mat:
                num = randint(1, 100)
        mat[l].append(num)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'{mat[l][c]} ', end='')
    print('')

verifica_matriz(*mat)

