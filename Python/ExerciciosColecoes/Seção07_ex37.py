
vet = []

for _ in range(0, 11):
    num = float(input())
    vet. append(num)

# Ordenando o vetor
for i in range(0, 11):
    for j in range(i+1, 11):
        if vet[i] > vet[j]:
            aux = vet[j]
            vet[j] = vet[i]
            vet[i] = aux

m = max(vet)
vet2 = []

# Passando para o vetor 2 o números ordenados até a posição 5
for i in range(0, 5):
    # passando cada número na forma de caractere/string
    vet2.append(str(vet[i]))

# Adiconando no vetor o maior número na forma de caractere
vet2.append(str(m))

# Ordenando o vetor de forma decrescente da posição 5 até a 10
for i in range(5, 11):
    for j in range(i+1, 11):
        if vet[i] < vet[j]:
            aux = vet[j]
            vet[j] = vet[i]
            vet[i] = aux


vet3 = []
# Passando para o vetor 3 os elementos do vetor 1 da posição 6 até a 10 na forma de caractere
for i in range(6, 11):
    vet3.append(str(vet[i]))

vet3 = vet2 + vet3
vet4 = []

# passando para o vetor 4 os caracteres do vetor 3 na forma de float
for i in range(0, 11):
    vet4.append(float(vet3[i]))

# Solução feita com 2 for's, sendo o primeiro para ordenar o vetor e o segunda para ordenar de forma descrescente
# da posição 5 até a 10.
print(vet)

# Solução feita com ordenação de vetor e transformação em caracteres, concatenando os caracteres para ficarem na posição
# Desejada e convertendo cada caractere em float novamente.
print(vet4)

