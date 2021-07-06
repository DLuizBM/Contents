def printar(*args):
    num = args[0]   # Passa para a variável num somento o número dentro da tupla
                    # e não a tupla inteira
    i = 1
    while i <= num:
        for _ in range(i):
            print(f'!', end='')
        print('')
        i = i + 1


numero_de_exclamação = int(input())
printar(numero_de_exclamação)