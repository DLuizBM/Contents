
def verifica_primo(N):
    """
    Passado um número N, essa função verifica quais números de 1 até N são primos!

    """
    cont = 0
    lista_de_numeros_primos = []

    for num in range(N+1):
        for i in range(1, num+1):
            if num % i == 0:
                cont = cont + 1
        if cont == 2:
            lista_de_numeros_primos.append(num)
        cont = 0
    print(lista_de_numeros_primos)


numero = int(input())
verifica_primo(numero)