
def gera_triangulo_latera(*args):
    t = 2 * args[0] - 1
    i = 0
    while i <= t:
        if i <= args[0]:
            for _ in range(i):
                print('*', end='')
        else:
            for _ in range(t - i + 1):
                print('*', end='')
        i = i + 1
        print('')


n = int(input())
gera_triangulo_latera(n)

# Saída
"""
n = 6

*
**
***
****
*****
******
*****
****
***
**
*
"""