"""import statistics

lista1 = [1, 2, 3, 4]
lista2 = [1, 2, 3, 4]

media1 = statistics.mean(lista1)
media2 = statistics.mean(lista2)

print(list(map(lambda x: x > media1, lista1)))
# saida: [False, False, True, True]
# map ao fazar comparações devolve valores booleanos
print(list(filter(lambda y: y > media2, lista2)))
# saida: [3, 4]
# filter ao fazer comparações devolve o valor

nomes = ['Messi', 'Mozer', 'Maradona', 'zico']
print(all([nome[0] == 'M' for nome in nomes]))
lista_criada =[]
for nome in nomes:
    if nome[0] == 'M':
        lista_criada.append(bool(nome[0]))
    else:
        lista_criada.append(not bool(nome[0]))
print((lista_criada))
# saida da lista_criada: [True, True, True, False]
# saida: false, pois faz a lista e dentro da lista verifica se todos são true


linha = "Uma vez flamengo" \
        "Sempre flamengo"
#print(linha.replace('U', 'Duas'))
LINHA = ''
for vogal in linha:
    if vogal.lower() == 'a':
       LINHA = LINHA + '*'
    elif vogal.lower() == 'e':
        LINHA = LINHA + '*'
    else:
        LINHA = LINHA + vogal
print(LINHA)



linha = "Uma vez Flamengo"
LINHA = ''
for letra in linha:

    if letra == letra.upper():
        LINHA = LINHA + letra
    else:
        LINHA = LINHA + letra.upper()
print(LINHA)


linha = 'São paulo: 1.300.000'
num = ''
for esp in linha:
    if esp == ':':
        a = linha.index(esp)
        for i in range(a+2, len(linha)):
            if linha[i] != '.':
                num = num + linha[i]
print(num)
print(type(num))
num = int(num)
print(type(num))



def retorna(num):
    lista = []
    for i in range(0, num):
        lista.append(i)
    return lista

for n in retorna(4): # retorna(4) recebe a lista [0, 1, 2, 4]
    print(n)



lista = [1, 2, 3, 4]
re = map(lambda x: x > 2, lista)
print(list(re))
# [False, False, True, True]
# map dessa forma devolve true or false

"""

mat = [[], []]
for l in range(0, 2):
    for c in range(0, 2):
        n = input()
        mat[l].append(n)

for l in range(0, 2):
    for c in range(0, 2):
        print(f'{mat[l][c]}', end='')
    print()