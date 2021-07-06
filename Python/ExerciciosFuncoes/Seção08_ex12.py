def soma_numero(*args):
    numero = list(str(args[0]))
    # Passando somente o args, será gerada a tupla (123, )
    # Passando args[0], somente o valor 123 será passado para a variável 'numero'
    # str transforma args[0] em string e list transforma em 123 em lista, sendo que
    # cada número é passado como caractere, dessa forma, ['1', '2', '3']

    print(numero)
    lista_de_numeros = []
    for num_lista in numero:
        lista_de_numeros.append(int(num_lista))
        # Transformando cada caractere em int e adicionando na lista 'lista_de_numeros'

    return sum(lista_de_numeros)


num = int(input())
print(soma_numero(num))