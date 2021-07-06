# Criando um diconário

aluno = {}

# Formas de adicionar elementos no dicionário

# Forma 1
# aluno[numero] = altura

# Forma 2 - Usada nesse programa
# novo = {numero: altura}
# aluno.update(novo)


for _ in range(0, 10):
    numero = int(input("Número do aluno: "))
    altura = float(input("Altura do aluno: "))
    aluno[numero] = altura

print(aluno)
# print(max(aluno # aluno.keys()))   # Pega a maior chave
# print(min(aluno))   # Pega a menor chave

# Pegando a chave do maior valor no dicionário
for chave, valor in aluno.items():
    if valor == max(aluno.values()):
        max_chave = chave

# Pegando a chave do menor valor no dicionário
for chave, valor in aluno.items():
    if valor == min(aluno.values()):
        min_chave = chave

print(f'Aluno mais alto: {max_chave} | Altura: {max(aluno.values())}.')
print(f'Aluno mais baixo: {min_chave} | Altura: {min(aluno.values())}.')