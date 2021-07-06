# coding=utf-8
"""
Módulo collections

Em um dicionário, não há garantia da ordem dos elementos

Ordered Dict: é um dicionário que nos garante a ordem de inserção dos elementos.



from collections import OrderedDict

dic = OrderedDict({'a': 1, 'b': 2, 'c': 3})

for chave, valor in dic.items():
    print(f'Chave: {chave} Valor: {valor}')

"""
# Entendendo a diferença entre dict e ordered dict

d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}

if d1 == d2:    # Será true, já que a ordem dos elementos não importa pro dicionário comum
    print(True)
else:
    print(False)

# Ordered dict
from collections import OrderedDict

od1 = OrderedDict({'a': 1, 'b': 2})
od2 = OrderedDict({'b': 2, 'a': 1})

print(od1 == od2)   # Será FALSE, pois para o ordereddict a ordem importa

