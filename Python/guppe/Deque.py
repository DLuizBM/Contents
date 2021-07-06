# coding=utf-8
"""
Módulo collections
Deque: É uma lista de alta performance.

a = "carro"
print(list(a))
# transformando a string em lista

"""
# Criando deques

from collections import deque

deques = deque('geek')
print(deques)

# Adicionando elementos no deque

deques.append('y')
print(deques)

deques.appendleft('z')  # Adiciona no começa da lista
print(deques)

deques.popleft()    # Remove do começo da lista e retorna o primeiro elemento
print(deques)