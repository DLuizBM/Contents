"""
REVERSED
- Não confundir com a função reverse de listas, que só funciona em listas
- Reversed funciona com qualquer iterável
- Retorna um list_reverseiterator, um objeto
- Assim como nas outras função, uma vez utilizado perde-se o valor
"""
lista1 = [1, 2, 3]
lista = reversed(lista1)
print(lista)
print(type(lista))
print(list(lista))
print(tuple(reversed(lista1)))

# Iterando

for letra in reversed('Flamengo'):
    print(letra, end='')
print('')
# Outra forma
print(''.join(list(reversed('Flamengo'))))
# reversed transformando em um lista de string, e join transforma uma lista de string em string novamente

print('Flamengo'[::-1])

# Fazendo um loop inverso

for n in reversed(range(0, 10)):
    print(f'{n} ', end='')
print()
for n in range(10, -1, -1): # de 10 até -1 diminuindo -1 a cada loop
    print(f'{n} ', end='')
