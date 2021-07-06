
A = []

# Adicionando na lista

for _ in range(0, 6):
    a = int(input())
    A.append(a)

print(A)

# Armazendo a soma das posições especificadas

soma = A[0] + A[1] + A[5]
print(soma)

# Modificando o vetor

A.insert(4, 100)
print(A)

# Mostrando o valor

for a in A:
    print(a)
