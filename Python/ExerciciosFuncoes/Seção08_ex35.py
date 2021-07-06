
def fatorial_quadruplo(*args):
    """
    Função que calcula o fatorial quádruplo
    :return: O fatorial quádruplo

    """
    fat = 1

    for i in range(1, (2 * args[0]) + 1):   # Calculno (2n)!
        fat = fat * i
    a = fat

    fat = 1

    for i in range(1, args[0] + 1):     # Calculo n!
        fat = fat * i
    b = fat

    fat = a / b

    return fat


num = int(input())
print(fatorial_quadruplo(num))

