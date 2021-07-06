 
"""
Dicionários

Em algumas linguagens de programação, os dicionários python são conhecidos por mapas.
Dicionários são coleções do tipo chave/valor (Mapeamento chave valor)

Nas listas e nas tuplas esse mapeamento(chave/valor = índice/valor) fica implícito:
lista = [1,2,3]
sabemos que:
 0, 1, 2  = índice
[1, 2, 3] = valor

Nos dicionários esse mapeamento fica explícito
Dicionários são representados pelas chaves {}

OBS: Sobre dicionários
    - Chave e valor são separados por ':'. 'chave1':'valor1', 'chave2':'valor2'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar todos os tipos de dado

# Criação de dicionários
# Forma 1 - Mais comum
paises = {'br': 'Brasil', 'pt': 'Portgual', 'eua': 'Estados Unidos'}
print(paises)
print(type(paises))

# Forma 2 - Menos comum

paises2 = dict(br='Brasil', pt='Portugal', eua='Estados Unidos')
print(paises2)


# Acessando elementos
# Dicionários NÂO são indexados
paises = {'br': 'Brasil', 'pt': 'Portgual', 'eua': 'Estados Unidos'}

# Forma 1 - Acessando via chave da mesma forma que lista/tupla
print(paises['br']) # O acesso é via chave(como se fosse o index), a chave é 'br'
print(paises['pt']) # O acesso é via chave(como se fosse o index), a chave é 'pt'
# Caso tentemos fazer o acesso com uma chave que não exista, o erro será KeyError

# Forma 2 - Acessando via get -- Recomendado
print(paises.get('br'))
print(paises.get('ru'))     # Como não existe essa chave, acessando via get não será
                            # apresentado erro, mas sim retonará o dado None

pais = paises.get('br')

if pais:
    print(f'Encontrei o {pais}')
else:
    print("Não encontrei.")

pais = paises.get('ru', 'Rússia')   # Pegue o país na chave 'ru', caso não encontre
                                    # coloque o valor 'Rússia'
print(f'Não encontrei o {pais}.')

# Busca de elementos no print

paises = {'br': 'Brasil', 'pt': 'Portgual', 'eua': 'Estados Unidos'}

print('br' in paises)
print('pt' in paises)
print('Estados Unidos' in paises)
# A busca sempre é feita pela CHAVE/ÍNDICE e não pelo valor
# Por isso a terceira busca resulta em false

if 'br' in paises:
    brasil = paises['br']
print(brasil)

paises = {'br': 'Brasil', 'pt': 'Portgual', 'eua': 'Estados Unidos'}

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive
# Listas, tuplas, dicionário, como chaves de dicionário

localidades = {
    (39.122, 39.789): 'Escritório em Tóquio',
    (50.234, 45.678): 'Escritório em NY',
    (11.098, 11.234): 'Escritório em São Paulo',
}
print(localidades)
# Tuplas são bastante interessantes para serem usadas como chaves de dicionário, pois são imutáveis

# Adicionar elementos em dicionário

# Forma 1 Mais comum
receita = {
    'jan': 100,
    'fev': 200,
    'mar': 300,
}
mes = input()
val = int(input())

receita[mes] = val
print(receita)

# Forma 2
novo = {'mai': 500}
receita.update(novo)
print(receita)
receita.update({'mai': 550})
print(receita)

# A forma de atualizar e inserir novos dados em um dicionário é a mesma.
# Em dicionário não podemos ter chaves repetidas.

# Remover dados de um dicionário
# Forma 1 - Mais comum
receita = {
    'jan': 100,
    'fev': 200,
    'mar': 300,
}
ret = receita.pop('fev')  # Sempre necessário passar a chave
print(receita)
print(ret)

# Ao remover um objeto esse objeto, com pop(), não é só removido, como seu valor é retornado

# Forma 2

del receita['jan']
print(receita)
# Se a chave não existir será gerado um KeyError
# Não retorna valor


# Utilizando listas e dicionário

carrinho = []
produto1 = {'Nome': 'Playstation', 'Preço': 2300.00}
produto2 = {'Nome': 'God of War', 'Preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Métodos de dicionários

# Limpar dicionário
d = {
    'a': 1,
    'b': 2,
    'c': 3,
}
print(d)

d.clear()
print(d)

# Copiando um dicionário

novo = d.copy()     # deep copy
print(novo)

novo['d'] = 4
print(d)
print(novo)
# Somente o 'novo' foi atualizado

novo = d        # Shallow copy
novo['d'] = 4

print(d)
print(novo)
# A modificação feita no 'novo' também foi feita em 'd'

"""

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'email', 'endereço'], 'desconhecido')
# Passando a lista, cada elemento da lista se tornou uma chave e 'desconhecido' se tornou o
# Valor para cada uma das chaves
print(usuario)
# O método fromkeys recebe dois parâmentros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado

nativo = {}.fromkeys('Brasileiro', ['Branco', 'Preto', 'Pardo'])
print(nativo)
# Irá iterar sobre cada letra de 'Brasileiro', o i e r só se repetirão 1 vez, pois em
# Dicionários python não há repetição de chave

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
# Criando números de 1 a 10 e colocando novo para cada 1 deles


