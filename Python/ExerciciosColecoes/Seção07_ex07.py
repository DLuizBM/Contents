vet = []

# Adicionando os valores na lista
for _ in range(0, 10):
    num = int(input())
    vet.append(num)

# Buscando o maior valor

a = max(vet)
print(a)

# Posição do maior valor

pos = vet.index(a)
print(pos)

# Invertendo o vetor

vet.reverse()
print(vet)