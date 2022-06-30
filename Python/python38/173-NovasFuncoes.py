"""
math.prod -> retorna o produto de um container numérico
math.isqrt -> devolve a raiz inteira de um número
math.dist -> retorna a distância euclidiana entre 2 pontos, 3d ou 2d
math.hypot -> retorna a hipotenusa ou norma euclidiana

import math
nums_v1 = [2, 3, 4, 5, 6]
nums_v2 = (2, 3, 4, 5, 6)

print(math.prod(nums_v1))
print(math.prod(nums_v2))
print(math.isqrt(17))
print(math.sqrt(17))

# Pontos 3d
p3d1 = (1, 2, 3)
p3d2 = (4, 5, 6)

# Pontos 2d
p2d1 = (1, 2)
p2d2 = (4, 5)

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))

import math

p3d1 = (1, 2, 3)
p2d2 = (4, 5)

print(math.hypot(*p3d1))
print(math.hypot(*p2d2))
# * serve para descompactar o container
# ex: [1, 2, 3] -> 1 2 3
print(*list(range(0, 5)))

"""
import statistics
# statistics.fmean -> calcula a média de números reais
print(statistics.fmean([1.2, 2.2, 3.2, 4.2]))
print(statistics.fmean([1, 2, 3, 4]))

# statistics.geometric_mean -> calcula a média geométrica
print(statistics.geometric_mean([1.2, 2.2, 3.2, 4.2]))
print(statistics.geometric_mean([1, 2, 3, 4]))

# statistics.multimode -> retorna o valor mais frequente em uma sequência
# se não há um valor que se repete mais, retorna o container inteiro
print(statistics.multimode([1.2, 2.2, 3.2, 4.2, 2.2]))
print(statistics.multimode([1, 2, 3, 4, 1]))
print(statistics.multimode("Lionel Messi"))
