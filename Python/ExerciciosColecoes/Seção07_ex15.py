vet = []

for _ in range(0, 10):
    num = int(input())
    vet.append(num)

# Fazendo a lista virar um conjunto para eliminar velores repetidos
c = set(vet)

# Transformando o conjunto em lista
vet = c.copy()
print(list(vet))

