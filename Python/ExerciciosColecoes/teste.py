"""
# Criando Matrizes

# Forma 1 - Com append
vet = [[], []]
# Cada lista dentro da lista representa uma linha

for l in range(0, 2): # Quantidade de linhas
    for c in range(0, 3): # Quantidade de colunoas
        num = int(input(f'elemento {l+1, c+1}: '))
        vet[l].append(num)
        # vet[l], pois está colocando o valor na linha
        # Ou seja, dentro do vetor[[],[]], vai preencher cada lista por vez
        # Assim o 'l' indica qual lista será preenchida. Por exemplo, se l = 0
        # Será preenchida a primeira lista dentro do vetor 'vet = [[]*,[]]' -- []* lista que está sendo preenchida
        # Quando l igual a 1, então será preenchida a segunda lista 'vet[[], []*].


print(vet)
print(vet[1][0]) # acessando um elemento da matriz pelo índice

# Forma 2

matrizes = [[0, 0, 0], [0, 0, 0]]

for l in range(0, 2):
    for c in range(0, 3):
        num = int(input(f'elemento {l+1, c+1}: '))
        matrizes[l][c] = num

print(matrizes)
# Printando a matriz
for l in range(0, 2):
    for c in range(0, 3):
        print(f'{matrizes[l][c]} ', end='')
    print('')

def nomes(n):
    print(n)
    # Saída : Pois é printado a string  inteira
    # maria
    # julia
    print(n[0])
    # Saída : Pois é printado somente o primeira caractere da string
    # m
    # j
nome = ['maria', 'julia'] # lista de strings, lembrando que cada string é um vetor de caracteres

nomes(nome[0])
nomes(nome[1])
# Passando dessa forma, cada nome é passado na forma de um vetor de caracteres(string)
"""
from random import randint

ordem = int(input())
mat = []

for _ in range(0, ordem):
    mat.append([])

for linha in range(0, ordem):
    for coluna in range(0, ordem):
        mat[linha].append(randint(0, 10))

for l in range(0, ordem):
    for c in range(0, ordem):
        print(f'{mat[l][c]} ', end='')
    print()


for i in range(0, ordem):
    for j in range(0, ordem):
        if 1 + j < ordem:
            print(mat[i][j+1])




