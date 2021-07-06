from random import randint
alternativas = ('a', 'b', 'c', 'd', 'e')
gabarito = ('b', 'c', 'c', 'd', 'e', 'a', 'a', 'd', 'b', 'e')

# Criando a matriz de respostas
resp = [[], [], []]
for l in range(0, 3):
    for c in range(0, 10):
        num = randint(0, 4)
        resp[l].append(alternativas[num])

for l in range(0, 3):
    for c in range(0, 10):
        print(f'{resp[l][c]} ', end='')
    print('')

print(gabarito)
# Gerando a matrícula de cada aluno
mat = []
for _ in range(0, 3):
    num = randint(10, 99)
    mat.append(num)

# Pontuação
pont = []
soma = 0
for l in range(0, 3):       # calculando a pontuação de cada aluno e colando em um vetor
    for c in range(0, 10):  # de acordo com a posição na matriz de respostas
        if resp[l][c] == gabarito[c]:
            soma = soma + 1
    pont.append(soma)
    soma = 0

# Aprovação
ap = []
for i in range(0, 3):
    if pont[i] >= 3:
        ap.append('Aprovado')
    else:
        ap.append('Reprovado')

print(f'Matrícula| Respostas            | Pontuação |    Resultado')
for l in range(0, 3):
    print(f'    {mat[l]}   |  ', end='') # end ='', o print para quando não houver mais informação
    for c in range(0, 10):               # sem isso, o print pularia uma linha e pararia
        print(f'{resp[l][c]} ', end='')
    print(f'|     {pont[l]}     |    ', end='')
    print(f'{ap[l]}', end='')
    print('')

