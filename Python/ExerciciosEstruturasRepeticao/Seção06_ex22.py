nota = int(input("Enter a grade.\n"))
lis = [0] * 10000000
i = 0
j = 0
while 10 <= nota <= 20:
    lis[i] = nota
    i = i + 1
    nota = int(input("Enter a grade.\n"))
    j = j + 1

a = int(len(lis))
soma = 0

for i in range(0, j): # poderiausar"a"também no lugar do "j"
    soma = soma + lis[i]

print(f"{soma/j}")