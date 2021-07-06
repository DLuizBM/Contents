# coding=utf-8
"""
Módulo collections: Default dict

Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre
que não houver uma valor definido. Caso tentemos acessar uma chave que não existe,
essa chave será criada e valor default será atribuído.

Diferente do dicionário(comum) em que ao acessar uma chave que não existe apresenta
KeyError.

OBS: lambdas são funções sem nome, que podem ou não receber parâmetros de entrada
e retornar valores.

# Todas as funções usadas no dicinonário comum são usadas no default dict
"""
from collections import defaultdict

dic = defaultdict(lambda: 0)

dic['curso'] = 'python'
print(dic)
print(dic['outro'])     # Em um dicionário comum seria apresentado um KeyError
print(dic)
