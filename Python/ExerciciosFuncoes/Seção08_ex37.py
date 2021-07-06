def hiperfatorial(*args):
    """
    Função que calcula o hiperfatorial
    :param args:

    """
    a = args[0]
    i = 1
    lista_numeros = []
    tot = 1
    while i <= a:
        for num in range(1, i+1):
            tot = tot * num
        lista_numeros.append(tot)
        i = i + 1
        tot = 1
    print(lista_numeros)

    tot = 1
    for num in lista_numeros:
        tot = tot * num

    print(tot)


N = int(input())
hiperfatorial(N)

