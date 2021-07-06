
vet = []
i = 0
while i < 10:
    num = float(input("Enter a real number: "))
    vet.append(num)
    i = i + 1

for i in range(0, 10):
    for j in range(i+1, 10):
        if vet[i] > vet[j]:
            aux = vet[j]
            vet[j] = vet[i]
            vet[i] = aux

print(vet)

