vet = []
k = 0
for _ in range(0, 10):
    num = int(input())
    vet.append(num)

print(vet)

vet2 = [0] * len(vet)

for i in range(0, 10):
    a = 0
    for j in range(0, 10):
        if vet[i] == vet[j]:
            a = a + 1
            if a == 2:
                vet2[k] = vet[i]
                k = k + 1

print(list(set(vet2)))