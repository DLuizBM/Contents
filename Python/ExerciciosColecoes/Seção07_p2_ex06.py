from random import randint

mat1 = [[], [], [], []]
mat2 = [[], [], [], []]
mat3 = [[], [], [], []]

for l in range(0, 4):
    for c in range(0, 4):
        num = randint(10, 100)
        mat1[l].append(num)

for l in range(0, 4):
    for c in range(0, 4):
        num = randint(10, 100)
        mat2[l].append(num)

for l in range(0, 4):
    for c in range(0, 4):
        if mat1[l][c] > mat2[l][c]:
            mat3[l].append(mat1[l][c])
        else:
            mat3[l].append(mat2[l][c])

print("Matriz 1!")

for l in range(0, 4):
    for c in range(0, 4):
        print(f'{mat1[l][c]} ', end='')
    print('')
print('\n')

print("Matriz 2!")
for l in range(0, 4):
    for c in range(0, 4):
        print(f'{mat2[l][c]} ', end='')
    print('')
print('\n')

print("Matriz 3!")
for l in range(0, 4):
    for c in range(0, 4):
        print(f'{mat3[l][c]} ', end='')
    print('')