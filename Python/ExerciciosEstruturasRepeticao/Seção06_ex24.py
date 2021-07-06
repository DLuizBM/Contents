num = int(input("Enter a integer. \n"))
lis = [0] * num
i = 0
for j in range(1, num):
    if num % j == 0:
        lis[i] = j
        i = i + 1
soma = 0

for k in range(0, i):
    soma = soma + lis[k]

print(soma)
