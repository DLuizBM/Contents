
vet = [0]*8
i = 0

while i < 8:
    num = float(input())
    vet[i] = num
    i = i + 1
    # Para utilizar esse método de inserção de elementos na lista, deve-se colocar a
    # estrutura indicada na declaração do vetor na linha 2 do programa.

print(vet)

x = int(input("Entre com a posição X."))
y = int(input("Entre com a posição Y."))

print(vet[x] + vet[y])