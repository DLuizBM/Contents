from random import randint

mat = [[], [], [], []]

for l in range(0, 4):
    for c in range(0, 4):
        num = randint(1, 20)
        mat[l].append(num)

print("Matriz original.")
for l in range(0, 4):
    for c in range(0, 4):
        print(f'{mat[l][c]} ', end='')
    print('')

for l in range(0, 4):
    for c in range(0, 4):
        if l == c: # Colocando o nos elementos acima da diagonal principal
            for coluna in range(c+1, 4):
                mat[l][coluna] = 0
print('\n')
print("Matriz transformada.")
for l in range(0, 4):
    for c in range(0, 4):
        print(f'{mat[l][c]} ', end='')
    print('')