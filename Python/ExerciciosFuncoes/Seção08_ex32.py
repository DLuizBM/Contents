def simplifica_fracao(num, den):
    lista_num = []
    if num > den:
        for i in range(1, num):
            if num % i == 0 and den % i == 0:
                lista_num.append(i)
    else:
        for j in range(1, den):
            if num % j == 0 and den % j == 0:
                lista_num.append(j)
    a = max(lista_num)
    print(f'A fração mais simplifica é: {num/a}/{den/a} !')

numerador = int(input())
denominador = int(input())

simplifica_fracao(numerador, denominador)