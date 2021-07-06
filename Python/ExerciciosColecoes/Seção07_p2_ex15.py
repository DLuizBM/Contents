from random import randint
# Criando a matriz
mat = [[], [], [], [], []]
alternativas = ('a', 'b', 'c', 'd', 'e')
# Uso de tuplas, pois essas alternativas não serão alteradas

for l in range(0, 5):
    for c in range(0, 10):
        # Preenchendo a matriz com as respostas de forma aleatória
        # 'indice' vai receber um número aleatório de 0 a 4 e esse número será passado
        # como o índice para selecionar uma das letras do vetor 'alternativas'
        indice = randint(0, 4)
        mat[l].append(alternativas[indice])

for l in range(0, 5):
    for c in range(0, 10):
        print(f'{mat[l][c]} ', end='')
    print('')

# Criando o vetor respostas
respostas = ('a', 'b', 'c', 'e', 'e', 'd', 'a', 'c', 'd', 'b')

# Comparando as respostas com o gabarito

# Criando o vetor com o resultado
resultado = []
soma = 0
for l in range(0, 5):
    for c in range(0, 10):
        if mat[l][c] == respostas[c]:
            soma = soma + 1
    resultado.append(soma)
    soma = 0


# Organizando tudo em um dicionário
from collections import OrderedDict

dic = OrderedDict({})

for i in range(0, 5):
    aluno = 'Aluno'
    pontos = resultado[i]
    novo = {aluno + ' ' + (str(i+1)): pontos}
    dic.update(novo)

for chave, valor in dic.items():
    print(f'{chave} --- Pontuação: {valor}')



