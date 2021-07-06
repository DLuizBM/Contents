
vet = []
vet2 = []

# Preenchendo o primeiro vetor

for _ in range(0, 10):
    num = int(input("Enter a integer."))
    vet.append(num)


for _ in range(0, 10):
    num = int(input("Enter a integer."))
    vet2.append(num)
    
print(vet)

vet3 = [0] * (len(vet)+len(vet2))

i = 0
for num in range(0, 20, 2):
    vet3[num] = vet[i]
    i = i + 1


i = 0
for num in range(1, 20, 2):
    vet3[num] = vet2[i]
    i = i + 1

print(vet2)
print(vet3)

