lis = [0] * 10
lis2 = [0] * 10
j = 0

for i in range(1, 11):
    lis[j] = i
    j = j + 1

tot1 = 0
for i in range(0, 10): # sempre lembrar que a lista começa na posição '0'
    tot1 = tot1 + (lis[i] * lis[i])

tot2 = 0
for i in range(0, 10):
    tot2 = tot2 + lis[i]

soma = tot2 * tot2

print(f"{soma - tot1}")