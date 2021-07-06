"""
Tipo float

Tipo real, decimal

OBS: O separador de casas decimais na linguagem python é o ponto

"""

# Errado do ponto de vista d0 float, mas gera uma tuple
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# É possível converter float para int
"""
OBS:  ao converter float para int perde-se precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
print(type(variavel))

