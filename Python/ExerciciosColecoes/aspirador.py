from random import randint

vet_estado = ['limpo', 'sujo']

ordem = int(input("Entre com a ordem da matriz: \n"))

posicao_sala = [i for i in range(0, ordem*ordem)]
print(posicao_sala)

mat = []
for i in range(0, ordem):
    mat.append([])
print(mat)


sala_estado = 0
p = 0

for i in range(0, ordem):
    for j in range(0, ordem):
        sala = "sala" + str(posicao_sala[p])
        sala_estado = vet_estado[randint(0, 1)]
        dic = {sala: {"estado": sala_estado, "robo": False}}
        mat[i].append(dic)
        p += 1


for i in range(0, ordem):
    for j in range(0, ordem):
        print(f"{mat[i][j]} ", end='')
    print()

# print(mat[0][0].get('sala0').get('estado'))
p = 0

mat[0][0]['sala0']['robo'] = True

for i in range(0, ordem):
    for j in range(0, ordem):

        sala = "sala" + str(posicao_sala[p])

        if mat[i][j].get(sala).get('estado') == 'limpo':
            print(f'A sala {sala} está limpa! \n')
            mat[i][j][sala]['robo'] = False
            if 1 + j < ordem:
                print(f'O robo está indo para a sala{p+1} \n')
                mat[i][1 + j][f"sala{p+1}"]['robo'] = True
            elif 1 + i < ordem:
                mat[1 + i][0][f'sala{p+1}']['robo'] = True
            elif i == j:
                print('Robo voltando para a sala0.\n')
                mat[0][0]['sala0']['robo'] = True

        elif mat[i][j].get(sala).get('estado') == 'sujo':
            print(f'A sala {sala} está suja! \n')
            print(f'O robo está limpando!\n')
            mat[i][j][sala]['estado'] = 'limpo'
            print(f'Sala limpa!')
            mat[i][j][sala]['robo'] = False
            if 1 + j < ordem:
                print(f'O robo está indo para a sala{p + 1} \n')
                mat[i][j + 1][f'sala{p+1}']['robo'] = True
            elif 1 + i < ordem:
                mat[i + 1][0][f'sala{p+1}']['robo'] = True
            elif i == j:
                print('Robo voltando para a sala0 \n')
                mat[0][0]['sala0']['robo'] = True

        p += 1


p = 0
for i in range(0, ordem):
    for j in range(0, ordem):
        sala = "sala" + str(posicao_sala[p])
        p += 1
        print(f'{mat[i][j][sala]["estado"], mat[i][j][sala]["robo"]} ', end='')

    print()


