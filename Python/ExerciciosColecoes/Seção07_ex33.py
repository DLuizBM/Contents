from collections import deque

vet = []

for _ in range(0, 5):
    num = int(input("Enter a integer: "))
    vet.append(num)

vet2 = []
for i in range(0, 5):
    if vet[i] != 0:
        vet2.append(vet[i])

print(vet2)








