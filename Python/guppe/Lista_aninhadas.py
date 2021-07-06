"""
Listas Aninhadas

'Vetores' multidimensionais
Matrizes.

"""

mat = [[1, 2, 3], [4, 5, 6]]

for l in mat:
    for c in l:
        print(f'{c} ', end='')
    print('')
# No primeiro for é passado uma lista, por vez, para 'l'
# No segundo for é passado um elemento da lista 'l', por vez, para a variável 'c'

[[print(f'{c}', end='')for c in l] for l in mat]
print()

# Jogo da velha

velha = [['0' if num % 2 == 0 else 'X' for num in range(1, 4)] for _ in range(1, 4)]
for num in velha:
    print(num)
