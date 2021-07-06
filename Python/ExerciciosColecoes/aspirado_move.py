"""ordem = int(input("Ordem: "))
mat = []

for _ in range(0, ordem):
    mat.append([])

for l in range(0, ordem):
    for c in range(0, ordem):
        mat[l].append('@')

comando = input('Comando: ')
comando.lower()
pos = [0, 0]

while comando != 'q':
    if comando == 'a':
        x = 1
        y = 0
        if pos[0] - x < 0:
            print('Este movimento não é possível!')
        else:
            pos[0] = pos[0] - 1
            print(pos[0])
            for l in range(0, ordem):
                for c in range(0, ordem):
                    if mat[l][c] == mat[pos[0]][pos[1]]:
                        mat[l][c] = '*'
                        print(f'{mat[l][c]} ', end='')
                    else:
                        print(f'{mat[l][c]} ', end='')
                print()
    elif comando == 's':
        x = 0
        y = 1
        if pos[1] + y > ordem - 1:
            print('Este movimento não é possível!')
        else:
            pos[1] = pos[1] + 1
            print(pos[1])

            for l in range(0, ordem):
                for c in range(0, ordem):
                    if mat[l][c] == mat[pos[0]][pos[1]]:
                        mat[l][c] = '*'
                        print(f'{mat[l][c]} ', end='')
                    else:
                        print(f'{mat[l][c]} ', end='')
                print()

    elif comando == 'd':
        x = 1
        y = 0
        if pos[0] + x > ordem - 1:
            print('Este movimento não é possível!')
        else:
            pos[0] = pos[0] + 1
            print(pos[0])

            for l in range(0, ordem):
                for c in range(0, ordem):
                    if mat[l][c] == mat[pos[0]][pos[1]]:
                        mat[l][c] = '*'
                        print(f'{mat[l][c]} ', end='')
                    else:
                        print(f'{mat[l][c]} ', end='')
                print()

    elif comando == 'w':
        x = 0
        y = 1
        if pos[1] - y < 0:
            print('Este movimento não é possível!')
        else:
            pos[1] = pos[1] - 1
            print(pos[1])

            for l in range(0, ordem):
                for c in range(0, ordem):
                    if mat[l][c] == mat[pos[0]][pos[1]]:
                        mat[l][c] = '*'
                        print(f'{mat[l][c]} ', end='')
                    else:
                        print(f'{mat[l][c]} ', end='')
                print()



    comando = input('Comando: \n')
"""
from random import randint

ordem = int(input())
posica_sala = [x for x in range(0, ordem*ordem)]
vet_estado = ['limpa', 'suja']
mat = []

for _ in range(0, ordem):
    mat.append([])

p = 0
for l in range(0, ordem):
    for c in range(0, ordem):
        sala = "sala" + str(posica_sala[p])
        dic = {sala: {"estado": vet_estado[randint(0, 1)], 'robo': False}}
        mat[l].append(dic)
        p += 1

for l in range(0, ordem):
    for c in range(0, ordem):
        print(f'{mat[l][c]} ', end='')
    print()

p = 0
mat[0][0]['sala0']['robo'] = True
for i in range(0, ordem):
    for j in range(0, ordem):
        sala = "sala" + str(posica_sala[p])
        if mat[i][j].get(sala).get('estado') == 'limpa':
            print(f'A sala{p} está limpa. \n')
            mat[i][j][sala]['robo'] = False
            if 1 + j < ordem:
                print(f'O robo está indo para a sala{p+1}. \n')
                mat[i][j + 1][f'sala{p+1}']['robo'] = True
            elif 1 + i < ordem:
                print(f'O robo está para a sala{p+1}. \n')
                mat[i + 1][0][f'sala{p+1}']['robo'] = True
            elif i == j:
                print('O robo está voltando para a sala0. \n')
                mat[0][0]['sala0']['robo'] = True

        elif mat[i][j].get(sala).get('estado') == 'suja':
            print(f'A sala{p} está suja. \n')
            print(f'O robo está limpando')
            mat[i][j][sala]['estado'] = 'limpa'
            print(f'A sala está limpa')
            mat[i][j][sala]['robo'] = False
            if 1 + j < ordem:
                print(f'O robo está indo para a sala{p+1}. \n')
                mat[i][j + 1][f'sala{p+1}']['robo'] = True
            elif i + 1 < ordem:
                print(f'O robo está indo para a sala{p+1}. \n')
                mat[i + 1][0][f'sala{p+1}']['robo'] = True
            elif i == j:
                print('O robo está voltando para a sala0. \n')
                mat[0][0]['sala0']['robo'] = True
        p += 1

p = 0
for l in range(0, ordem):
    for c in range(0, ordem):
        sala = "sala" + str(posica_sala[p])
        print(f'{mat[l][c][sala]["estado"], mat[l][c][sala]["robo"]} ', end='')
        p += 1
    print()









