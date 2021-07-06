"""
List Comprehension

- Utilizando list comprehension podemos gerar novas listas com dados processados
a partir de outro iterável

Sintaxe
[(para cada) dado for cada iterável]


# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
# Multiplique por 10 cada numero na 'lista numeros' e crie a 'lista res'

print(res)

# Utilizando com funções


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)

nome = 'Ayrton Senna'
a = [letra.upper() for letra in nome]
print(''.join(a))

amigos = ['hamilton', 'alonso', 'prost', 'senna']
print([amigo.title() for amigo in amigos])
# Tittle transforma a primeira letra em maiúsculo

print([bool(valor) for valor in [0, '', True, 1, 2]])

"""

# É possível colocar estruturas lógicas condicionais em list comprehensions

lista = [1, 2, 3, 4, 5, 6]

par = [numero for numero in lista if not numero % 2]
# Coloque o número na lista (par) se o número não tem resto de 2 (if not numero % 2)
print(par)
impar = [numero for numero in lista if numero % 2]
# Coloque o número na lista (impar) se o número tem resto de 2 (if numero % 2)
print(impar)

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in lista]
# Multiplique por 2 se o número for par, caso não, divida por 2
print(res)

print([num for num in lista if num % 2 == 0])