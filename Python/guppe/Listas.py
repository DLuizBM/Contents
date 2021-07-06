
"""
Listas em python funcionam como vetores/matrizes(arrays), para outras linguagens
a diferença é de serem dinâmicos e de poder colocar qualquer tipo de dado

Liguagem C/JAVA: Arrays
    -Possuem tamanho e tipo fixo
    Ou seja, se for criado um array do tipo int com tamanho 5, este array será sempre
    do tipo int e terá no máximo 5 valores

No python:
-Dinâmico:
    não possui tamanho fixo: Ou seja, podemos criar a lista e ir adicionando elementos
-Qualquer tipo de dado: Listas não possuem tipo de dado fixo: Ou seja, podemos colocar
    qualquer tipo de dado dentro

-Listas são representadas por []

-Listas são mutáveis, ou seja, elas podem mudar constantemente



num = 7
if num in lista4:
    print(f"Encontrei o número {num}.")
else:
    print(f"Não encontrei o número {num}")

# ordenando lista
lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

# contando a ocorrência de um número/caractere numa lista

print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em lista
# Para adicionar elementos em listas usamos a função append
# Com o append só é possível adicionar um elemento por vez

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1])# está passando um elemento em forma de lista
                        # Coloca a lista como elemento único
                        #atribiu ao final da lista
print(lista1)
if [8, 3, 1] in lista1:
    print("Encontrei a lista.")

lista1.extend([123, 44, 67])# coloca cada elemento da lista como valor adicional
                            # diferente do append
                            # atribui ao final da lista

print(lista1)

lista1.extend('geek')
print(lista1)

# Podemos inserir um elemento na lista informando a posição do índice

lista1.insert(2, 'novo valor') # Não substitui o valor da posição 2
                               # o mesmo é deslocado para a direita
print(lista1)

# Podemos juntar listas

lista6 = lista1 + lista2
lista1.extend(lista2)
print(lista6)
print(lista1)

# Invertendo listas
print(lista1[::-1])
print(lista2[::-1])
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Copiando listas
lista6 = lista2.copy()
print(lista6)

# Tamanho de lista

a = len(lista1)
print(a)

# Removendo o último elemento de uma lista
# OBS: O pop não somente remove o última elemento como também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Removendo elemento pelo índice
# Os elementos a direita deste índice serão deslocados para a esquerda
# Se não houver elemento no índice especificado, teremos o erro IndexError
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos da lista
print(lista5)
lista5.clear()
print(lista5)

# Podemos repetir os elementos de uma lista
print(lista5)
lista5 = lista5 * 3
print(lista5)


# Podemos converter uma string para uma lista

# exemplo1
curso = 'programação em python'
print(curso)
curso = curso.split()
print(curso)
# Por padrão o split() separa os elementos pelos espaços entre eles.

# exemplo2
curso = 'programação,em,python'
print(curso)
curso = curso.split(',') # especificando o separador
print(curso)

# Convertendo uma lista em string

lista6 = ['programação', 'em', 'python']

print(lista6)

# Abaixo estamos falando: pegue a lista6 coloque um espaço entre os elementos e transforme em string
curso = ' '.join(lista6)
print(curso)
# Abaixo estamos falando: pegue a lista6 coloque um $ entre os elementos e transforme em string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Geek', 'd', 1234567890]
print(lista6)
print(type(lista6))

# Iterando sobre listas

for elemento in lista1:
    print(elemento)

for i in range(0, 8):
    print(lista1[i])

soma = ''
for i in lista2:
    soma = soma + i
print(soma)

soma = ''
for i in range(0, 15):
    soma = soma + lista2[i]
print(soma)


# Adicionando elementos na lista
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair.")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Na lista fazemos o acesso de forma indexada

cores = ['verde', 'branco', 'azul', 'amarelo']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Acesso de forma inversa

print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

for cor in cores:
    print(cor)

i = 0

while i < len(cores):
    print(cores[i])
    i = i + 1


# Gerar índice em um for

cores = ['verde', 'branco', 'azul', 'amarelo']
# O enumerate gera pares de chave(índice/posição ao qual o valor está) e valor
# No exemplo abaixo a variável(índice) vai dar a posição do valor e a variável
# cor vai dar o valor que está naquele posição
for indice, cor in enumerate(cores):
    print(indice, cor)

# estamos criando uma lista que vai receber em cada posição um par de chave e valor
# que foi criado pelo enumarate a partir da lista cores
color = list(enumerate(cores))
print(color)


# Listas aceitam repetição

lista = list() #criando lista vazia
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)

print(lista)

# Encontrar índice de um elemento em uma lista

numero = [5, 6, 7, 8, 5, 9, 10, 7]

# Em qual índice da lista está o número 6?
print(numero.index(6))

# Caso o valor não esteja na lista, será apresentado um ValueError
# Se houver um elemento repetido na lista, a função retornará o índice do primeiro elemento
print(numero.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numero.index(5, 1)) # Qual o indice do '5', contando agora a partir do índice 1
                          # e não mais do índice '0'. Contando a partir de 1, ele
                          # vai encontrar uma valor 5 no índice 4

print(numero.index(7,3)) # O mesmo acontece para o valor '7', contando a partir do
                         # índice 3, o próximo valor que ele acha se encontra no
                         # índice 7

# Podemos fazer a busca do índice entre um range de índices inicial e final
print(numero.index(7, 0, 3)) # Faça umas busca do índice do valor '7', entre os
                             # índices 0 e 3. Como o índice do valor 7 se encontra
                             # entre os índices 0 e 3, ele retornará o valor do índice 7 que é 2


# Slicing

# Lista[início: fim: passo]
# range(início: fim: passo)

# Trabalhando com slice de lista com o parâmentro início

lista = [1, 2, 3, 4, 5]

print(lista[1::]) # iniciando no índice 1 e pegando todos os restantes
                 # vai imprimir a partir do elemento '2'
print(lista[-1::]) # A lista é circular, ao colocar o '-1', ele vai printar o elemento 5

# Trabalhando com slice de lista com o parâmentro início

print(lista[:3:]) # começa em 0 e pega até o elemento 3 - 1 = 2
                  # Printa até o índice 2


print(lista[1:4:]) # começa no índice 1 e vai até o índice 4 - 1 = 3

# Trabalhando com slice de lista com o parâmentro passo

print(lista[0::2]) # começa no índice 0 e vai até o final de 2 em 2
print(lista[1::2])
print(lista[5::-1])
# se o valor inicial for maio que o número de elementos no array
# vai pegar a partir do último elemento

# Invertendo valores em uma lista

nomes = ['Geek', 'university']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes.reverse()
print(nomes)

# Soma, valor max, valor min, tamanho

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))



# Podemos transformar listas em tuplas

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(lista))

# Desempacotamento de lista

lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# Se tivermos mais ou menos elementos para desempacotar do que variáveis para receber
# os valores, será informado ValueError

lista1 = [1, 99, 4, 27, 15, 22, 3, 1]

lista2 = ['g', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Copiando uma lista para outra(Shallow copy e Deep copy)
# Forma 1 - Deep copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)

# Utilizando lista.copy() copiamos os dados de uma lista para outra, mas elas
# ficaram totalmente independentes, ou seja, modificar uma lista não afeta a outra.
# Isso em python é chamado de Deep Copy (cópia profunda).

# Forma 2 Shallow  Copy

lista = [1, 2, 3]

nova = lista
print(nova)
nova.append(4)

print(lista)
print(nova)

# Utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista
# Mas após realizar modificações em uma das listas, essa modificação se refletiu
# em ambas as listas. Isso em python é chamado de Shallow Copy.
"""

lst = [1, 3, 5, 7]
lst.remove(1) # remove o objeto, lança execeção caso o objeto não exista
lst.pop(2) # remove pelo index
print(lst)