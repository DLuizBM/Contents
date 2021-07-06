vet = []
vet2 = []

for _ in range(0, 10):
    num = float(input())
    if 0 <= num <= 50:
        vet.append(num)

for num in vet:
    if num % 2 != 0:
        vet2.append(num)

print(vet)
print(vet2)

    


