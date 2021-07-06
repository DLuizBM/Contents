"""
Dictionary comprehension

{chave: valor for valor in iterável}

dic = {'a': 2, 'b': 4}

print({chave: valor ** 2 for chave, valor in dic.items()})


# Trabalhando dicionários e lista(poderia ser qualquer coleção)

lista = [1, 2, 3]

quadrado = {valor: valor**2 for valor in lista}
print(quadrado)

"""

lista = [1, 2, 3]
dic = {num: ('par' if num % 2 == 0 else 'impar') for num in lista}
print(dic)


dic = {'a': 2, 'b': 4}

print({chave: valor ** 2 for chave, valor in dic.items()})

from collections import OrderedDict
new_dict = OrderedDict()
print({key: key * 2 for key in range(1, 11)})