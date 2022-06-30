"""
O operador Walrus permite fazer a atribuição e o retorno de valor numa mesma expressão

Sintaxe

variável := expressão


# Exemplo

print(name := "Lionel Messi")

from typing import List
# Exemplo python 3.7
cesta: List[str] = []

fruta: str = input('Digite o nome da fruta: ')
while fruta != 'uva':
    cesta.append(fruta)
    fruta: str = input('Digite o nome da fruta: ')
"""
from typing import List

cesta: List[str] = []
# Exemplo python 3.8 com walrus
# while(fruta := input('Digite o nome da fruta: ')) != 'uva':
while((fruta := input('Digite o nome da fruta: ')) != 'uva'):
    cesta.append(fruta)
print(cesta)