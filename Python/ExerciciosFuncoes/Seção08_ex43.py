from random import randint

def preenche_aleatório(*args):
    """
    Função que preenche uma lista com números inteiros aleatórios
    :param args:
    :return:
    """
    lista = []
    for i in range(0, 10):
        args = randint(91, 100)
        if args in lista:
            while args in lista:
                args = randint(91, 100)
        lista.append(args)
        lista.sort()
    return lista


vet = []
print(preenche_aleatório(*vet))