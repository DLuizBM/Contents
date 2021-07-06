    # coding=utf-8
"""
Conjuntos:

-Em qualquer linguagem de programação, estamos fazendo referência a teoria dos conjuntos
da matemática

-Em python os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:
-Sets(conjuntos) não possuem valores duplicados:
-Sets não possuem valores ordenados:
-Elementos não são acessados via índice, ou seja, não são indexados.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não
nos importamos com a ordenação deles. Quando não precisamos nos preocupar com chaves,
valores e items duplicados.

Os conjuntos são refereciados com {}.

Diferença entre conjuntos(Sets) e Mapas{dicionários} em python:
    - um dicionário tem chave/valor;
    - um conjunto tem apenas valor.

# Definindo um conjunto

# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})     # Há números repetidos
print(s)
print(type(s))
# OBS: Ao criar um conjunto, caso seja adicionado um elemento já existente, o mesmo
# será ignorado sem gerar erro e não fará parte do conjunto

# Forma 2
s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
print(s)
print(type(s))

lista = [1, 2, 3, 4, 5, 5, 6, 7, 2, 3]
print(lista)
print(set(lista))   # Gerando um set da lista, excluirá da lista todos os elementos repetidos

# Verificando se determinado elemento está no conjunto
if 3 in s:
    print("Está no conjunto.")
else:
    print("Não está no conjunto")


# Importante lembra que além de não termos valores duplicados, não temos ordem

# Conjunto não aceitam valores duplicados
s = {99, 2, 34, 12, 1, 44, 5, 5, 12}
print(f'Conjunto:{s} com {len(s)} elementos.')

# Listas aceitam valores duplicados
l = [99, 2, 34, 12, 1, 44, 5, 5, 12]
print(f'Lista:{l} com {len(l)} elementos.')

# Tuplas aceitam valores duplicados
t = (99, 2, 34, 12, 1, 44, 5, 5, 12)
print(f'Tuplas:{t} com {len(t)} elementos.')

# Dicionários não aceitam chaves duplicadas
d = {}.fromkeys([99, 2, 34, 12, 1, 44, 5, 5, 12], 'dic')
print(f'Dicionários:{d} com {len(d)} elementos.')

# Assim como as outras coleções, os conjuntos também aceitam qualquer tipo de dado
s = {1, 2.4, 'b', True, "Conjuntos"}

# Podemos iterar em um conjunto normalmente

for valor in s:
    print(valor)

# Usos interessantes com sets
# Retirando duplicidades em lista com strings
cidades = ['São Paulo', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Belo Horizonte', 'Cuiabá']
print(cidades)
print(set(cidades))     # A ordenação nos conjuntos é aleatótia, não será impresso
                        # na ordem em que é passado
print(len(set(cidades)))

# Adicionando elementos em um conjunto

s = {1, 2, 3}
print(s)
s.add(4)
print(s)
# Se tentarmos adicionar o 4 novamente, este não será adicionado

# Remover elementos num conjunto

# Forma 1
s = {1, 2, 3}
print(s)
s.remove(3)     # Não é índice, e sim o próprio valor a ser removido, pois conjuntos não são indexados
print(s)
# Caso o valor não seja encontrado, será gerado um KeyError
# Nenhum valor é retornado, diferente de outras coleções que ao se remover um valor
# Esse valor é retornado

# Forma 2

s.discard(2)
print(s)
#  OBS: Se nenhum valor for encontrado, não será gerado nenhum erro

# Copiando conjuntos

s = {1, 2, 3}
print(s)
cop = s.copy()  # Deep copy
cop.add(4)
print(cop)
print(s)

cop = s
cop.add(5)     # Shallow copy
print(cop)
print(s)

# Podemos remover todos os elementos de um conjunto

s = {1, 2, 3}
print(s)
s.clear()
print(s)

# Métodos matemáticos aplicados nos conjuntos

# União de conjuntos
# Forma 1

estudantes_java = {'Patricia', 'Marcos', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_python = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

unico = estudantes_java.union(estudantes_python)
print(unico)

# Forma 2
unicos = estudantes_python | estudantes_java
print(unicos)

# Intersecção de conjuntos
# Forma 1

ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)

# Forma 2
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Estudantes que estão em um curso, mas não estão no outro
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Soma, valor máximo, valor mínimo, tamanho

s = {1, 2, 1, } # type set

print(sum(s))   # Lembra que como não há valores repetidos, só irá somar os valores diferentes
print(max(s))
print(min(s))
print(len(s))   # Tamanho só será dado pelos valores diferentes
print(type(s))



