num1 = int(input())
num2 = int(input())

if num2 > num1:
    for _ in range(1):
        break

lis = [0]*num2
j = 0

for i in range(num1, num2+1):
    if i % 2 != 0:
        lis[j] = i
        j = j +1

soma = 0

for k in range(0, j):
    soma = soma + lis[k]

print(soma)