
vet = []
vet2 = []
for _ in range(0, 2):
    num = int(input())
    vet.append(num)

for indice, valor in enumerate(vet):
    add = 0
    # Condição para saber se o número é primo
    for i in range(1, valor+1):
        if valor % i == 0:
            add = add + 1
    if add == 2:
        # Add o elemento no vetor
        vet2.append(valor)
        # Add o indice do elemento no vetor
        vet2.append(indice)

print(vet2)
vet3 = vet2.copy()
print(vet2[0::2], vet3[1::2])

