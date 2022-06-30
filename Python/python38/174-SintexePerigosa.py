"""
== -> usado para checar valor
is -> usado para checar se os objetos são iguais, ou seja, se os objetos tem a mesma referência
"""

class Person:
    pass

p = Person()
p2 = p

if p is p2:
    print("It is person")
else:
    print("It is not a person")