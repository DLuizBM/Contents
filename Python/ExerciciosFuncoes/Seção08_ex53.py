from random import randint

def verifica_identidade(ordem, *args):
    lista_1 = []
    lista_0 = []
    for l in range(0, ordem):
        for c in range(0, ordem):
            if l == c:                      # Só a diagonal principal pode ter 1, por isso essa condição
                lista_1.append(args[l][c])  # é necessário, pois poder haver matrizes com 0s e 1s, porém
            else:                           # algum 1 pode não estar na diagonal principal
                lista_0.append(args[l][c])

    if sum(lista_1) == ordem and sum(lista_0) == 0:
        print("É identidade!")
    else:
        print("Não é identidade.")

# Criando uma matriz quadrada de ordem N
# Basta criar uma lista vazia e fazer um for com N loops
# Para cada loop basta adicionar na lista uma nova lista

ordem_matriz = int(input())
lista = []
for _ in range(ordem_matriz):
    nova_lista = list()
    lista.append(nova_lista)
print(lista)

for l in range(0, ordem_matriz):
    for c in range(0, ordem_matriz):
        num = int(input())
        lista[l].append(num)

for l in range(0, ordem_matriz):
    for c in range(0, ordem_matriz):
        print(f'{lista[l][c]} ', end='')
    print('')

verifica_identidade(ordem_matriz, *lista)


