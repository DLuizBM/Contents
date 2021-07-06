
num = [0] * 10
i = 0
for _ in range(1, 11):
    a = int(input())
    num[i] = a
    i = i + 1 # usar essa estrutura (i = i + 1) para passar valores
              # digitados para a lista

b = min(num)
c = max(num)

print(f"Menor valor {b}.")
print(f"Maio valor {c}. \n")