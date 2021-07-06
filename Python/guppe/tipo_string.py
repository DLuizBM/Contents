"""
Recebendo dados do usuário

Todo dado recebido via input() é string

Em pyhton, string é tudo que estiver em:

Aspas simples: 'Angelina'
Aspas duplas: "Angelinas"
Aspas simples triplas: '''Angelina'''

nome = 'Geek university'
print(nome)
print(type(nome))

nome = "gina's bar"
print(nome)
print(type(nome))

nome = 'Angelina \n
Jolie'
print(nome)
print(type(nome))
"""
# Aspas duplas triplas: """Angelina"""

nome = 'Geek university'

print(nome[0:4])
# imprime o Geek, vai até a posição 3 do array, apesar do
# 4 estar inserido, o método pega a posição anterior ao 4, ou seja 3

print(nome[5:15])
# imprime o University, vai até a posição 14 do array, apesar do
# 15 estar inserido, o método pega a posição anterior ao 15, ou seja 14

print(nome.split()[0])
print(nome.split()[1])

"""
[::-1] comece do primeiro elemento,vá até o último elemento e inverta
"""
print(nome[::-1])
name = "Divino"

print(name[-2:-5:-2])
"""
comece na posiço -2 e váaté  -5, com passo de -2
contando a partir do 0, o é 1, n é-2 e assim por diante.
passo negativo só funciona quando a iteraçã está indo da esquerda pra direita.
"""