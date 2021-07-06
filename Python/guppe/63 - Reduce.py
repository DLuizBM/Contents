"""
REDUCE

OBS: a partir da versão 3 do python, a reduce não é mais uma função integrada(built-in)
deve-se importar e utilizar pelo módulo functools

- Deve-se utilizar a reduce() em casos realmente necessários, na maioria dos casos
um loop for é mais legível
- Passado 2 parâmetros -> reduce(função, iterável)

- Como é utilizado:

num = [a1, a2, a3, a4, ..., an]
def soma(x, y):
    return x + y
- Aplicando o reduce, a função faz os seguintes passos:
1 - res1 = f(a1, a2)
2 - res2 = f(res1, a3)
3 - res3 = f(res2, a4)
.
.
.
n - resn = f(resm, an)
No final ela devolve a soma de todos os valores, mas o processo de execução de reduce
é esse, opera de 2 em 2 elementos, como num Loop

"""

# Exemplos

from functools import reduce

num = [1, 2, 3, 4, 5, 6]

multi = lambda x, y: x * y
calc = reduce(multi, num)
print(calc)

print(reduce(lambda x, y: x * y, num)) # Usar pra fazer um teste de python
# O resultado é numérico, não é preciso converter pra lista ou outra coleção

fat = 1
for n in num:
    fat = fat * n
print(fat)

# fatorial de 7

num = list(range(1, 8))

fat = reduce(lambda x, y: x * y, num)
print(fat)

