vet = []

for _ in range(0, 10):
    num = float(input("Enter a number."))
    vet.append(num)

for i in range(0, 10):
    if vet[i] < 0:
        vet[i] = 0

print(vet)