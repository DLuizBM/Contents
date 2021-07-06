def arvore(*args):
    """
    Função cria uma árvore de 10 camada, preenchidas por 2*n - 1 no loop
    :param args: *args
    :return:sem retorno
    """
    i = 0
    j = 0
    while i <= args[0]:
        for _ in range(args[0] - j):# Para N = 10, args[0] é 10, dessa forma, no primeiro
                                    # loop desse for serão dados 10 espaços, no segundo 9
                                    # no terceiro 8 e assim por diante...
            print(' ', end='')
        for _ in range(2*i - 1):
            print('*', end='')
        print('')
        i = i + 1
        j = j + 1


N = int(input())
arvore(N)

"""
Com N=10, a árvore será:

         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************

"""