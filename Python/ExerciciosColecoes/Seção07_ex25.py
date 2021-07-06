
"""
a = 'carro de malandro'
a = list(a)
print(a)
Saída: ['c', 'a', 'r', 'r', 'o', ' ', 'd', 'e', ' ', 'm', 'a', 'l', 'a', 'n', 'd', 'r', 'o']
# O list() separa cada elemento da string em CARACTERE e coloca cada um em uma posição
# da lista

a = "Carro de malandro"
curso = a.split()
print(curso)
Saída: ['Carro', 'de', 'malandro']
# O split() separa cada elemento da string, pelo espaço, e coloca cada um em uma
# posição da lista. 
"""
vet = []
for num in range(1, 10000, 1):
    # convertendo o inteiro em string
    a = str(num)
    # separando a string por elemento e colocando em uma lista
    a = list(a)
    # print(a)
    ult = a.pop()
    if num % 7 != 0 and ult != '7' and len(vet) < 100:
        vet.append(num)
print(vet)
print(len(vet))
