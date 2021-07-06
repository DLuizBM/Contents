"""
Entendendo o *args

-É um parâmetro, como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterísco.
Exemplo:
*xis

-O parâmetro *args utilizado em uma função, coloca os valores extras informados
como entrada em uma tupla. Então desde já, lembre-se que tuplas são imutáveis

# Entendendo o args


def soma_total(*args):
    total = 0                                # Passando a posição de args, como se fosse um vetor
    for num in args:                         #total = 0
        total = total + num                  #i = 0
    return total                               #for num in range(0, len(args)):
                                                    #total = total + args[i]
                                                    #i = i + 1
                                                #return total


print(soma_total(1))
print(soma_total(2, 2))
print(soma_total(3, 2, 3))
print(soma_total(4, 2, 3, 4))
# É possível passar para a função quantos argumentos quisermos, usando o args

# Entendendo o args


def jogo_da_velha(*args):
    if 'Jogo' and 'velha' in args:
        print("Este é o jogo da velha!")
    else:
        print("Este não é o jogo da velha.")


jogo_da_velha('xadrez', 'dama')
jogo_da_velha('dominó')
jogo_da_velha('velha', 'Jogo')



"""


def soma(*args):
    print(args)
    return sum(args)


print(soma(1, 2, 3, 4))

numeros = [1, 2, 3, 4, 5]

# print(soma(numeros))
# Gera erro, pois o args transforma tudo em tuplas, dessa forma, a lista passada
# Será um elemento de uma tupla e não será feita a soma
# Saída: ([1, 2, 3, 4, 5],)

# Para resolver esse problema será necessário desempacotar a lista

# Forma 1
num1, num2, num3, num4, num5 = numeros

print(soma(num1, num2, num3, num4, num5))

# Forma 2 - Mais usada

print(soma(*numeros))
# Dessa forma estou indicando para o python que estou trabalhando com uma lista
# ou coleção, podendo ser tuplas, conjuntos e etc,
# e que o python precisa desempacotar.

