"""
for item in iterável:
    //

Exemplos de iteráveis
String = 'Geek'
Lista = [1,3,5,6,7,9]
range = (1,10)

# Exemplo de for (string)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for letra in nome:
    print(letra)

# Exemplo de for (lista)
print("\n")

for numero in lista:
    print(numero)

# Exemplo de for (range)
print("\n")

for numero in numeros:
    print(numero)
# range(valor_inicial, valor_final)
# OBS: valor final não é inclusivo.
# range(1, 10) = 1,2,3,4,5,6,7,8,9.


//////////////////////////////////////////

nome = 'Geek University '
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# enumerate:
# (0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' ')...

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _,letra enumerate(nome):
    print(letra)
# OBS: quando não precisamos de um valor podemos descartar usando '_'

for l in enumerate(nome):
    print(l)

for letra in enumerate(nome):
    print(letra[0])# mostra somente os números


print("Quantas vezes esse loop deve ser executado?")

qtd = int(input('\n'))

for n in range(1, qtd+1):
    print(f"loop {n}")

soma = 0
for n in range(1, qtd+1):
    num = int(input(f"Digite o valor {n}/{qtd}:"))
    soma = soma + num
print(f"A soma é {soma}")

nome = "Geek University"

for letra in nome:
    print(letra, end='')
    # para imprimir sem pular espaço entra as letras

"""

# emoji: U+1F60D
# Modificado: U000F60D

for n in range(1,4):
    for n in range(1, 11):
         print('\U0001F60D' * n)

str = "Astra"

for value in range(len(str[0]) - 1, len(str) - 2):
    print(str[value])
x = str.strip("Asra")
# com strip é possível tirar os elementos do início e fim de uma string
# sendo que eles devem estar na ordem, por exemplo, As são as 2 primeiras letras
# ra, são as duas últimas
print(x)















