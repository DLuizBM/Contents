def fatorial_expoencial(exp):
    """
    A função calcula o exponencial fatorial de um número, ou seja, dado um número
    inteiro N, fatorial exponencial de N é: N^(N-1)^(N-2)^(N-3)...
    :param exp:

    """
    i = 1
    A = exp
    lista_potencia = []
    for e in range(1, exp + 1):
            lista_potencia.append(e)
            i = i + 1

    print(lista_potencia)
    print(len(lista_potencia))

    for num in range(0, len(lista_potencia)):          # For indo de 0, até o tamanho da lista - 1
            if exp - num - 2 > 0:                      # exp-num-2 = cáculo para iniciar e parar os exponenciais
                A = A ** lista_potencia[exp - num - 2] # 'A' já iniciado com o valor N(exp, no código
                print(A)                               # Será elevado e pelo expoente em questão e atualizado
                # lista_potencia[exp - num - 2]: Nos vetores as posições variam de 0 até TamanhoVetor-1
                # a subtração por 2 no início é para fazer com que o primeiro expoente comece uma
                # Unidade abaixo do número passado, exemplo: Se o número N passado para a função
                # For 4 (a lista será [1, 2, 3, 4]), então o primeiro expoente de ser 3, na lista o número 3 está na posiçao 2
                # Logo o programa deve buscar em lista[2], para buscar o elemento 3
                # Se a expressão fosse (exp - num - 1), a busca iniciaria em lista[3] = 4
                # num é a variável responsável por diminuir o índice para buscar os outros elementos na lista


num = int(input())
fatorial_expoencial(num)