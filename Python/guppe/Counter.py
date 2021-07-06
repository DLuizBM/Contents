# coding=utf-8
"""
Módulo collections - counter

Collections - High-performance Contêiner Datetypes

Counter - recebe um iterável como parâmetro e cria um objeto do tipo collections counter
que é parecido com um dicionário, contendo como chave o elemento da lista passada como
parâmetro e como valor a quantidade de ocorrências desse elemento


# Realizando o importe
from collections import Counter

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 66]

res = Counter(lista)
print(type(res))
print(res)

# Saída: Counter({1: 5, 3: 5, 2: 4, 4: 3, 5: 3})
# Veja que, para cada elemento da lista o Counter colocou como chave os elementos na lista
# E colocou como valor a ocorrência de cada um desse elementos
# o elemento 1 por exemplo, ocorre 5 vezes na lista, já o 66 apenas 1 vez


lista = ['Geek university']
lista2 = ['g', 'e', 'e', 'k']

print(Counter(lista))
# Counter({'Geek university': 1})
print(Counter(lista2))
# Counter({'e': 2, 'g': 1, 'k': 1})

"""

# Utilizando o counter

# Realizando o importe
from collections import Counter


musica = """Desde o princípio
      Dm           C        Dm           C
Antes mesmo que a terra começasse a existir
Dm         C            Dm C Dm C
O Verbo estava junto a Deus
Dm       C
Veio ao mundo
       Dm        C             Dm            C
E pra não abandonar-nos nesta viagem nos deixou
Dm         C         Dm  C
Todo a si mesmo como pão

Dm          C       F
Verbum caro factum est
        C           Dm
Verbum panis factum est
            C       F
Verbum caro factum est

        C           Bb    C
Verbum panis factum est

     F    C         Dm             C
E aqui partes o teu pão em meio a nós
      Bb          F    Gm            C4   C
Todo aquele que comer  não terá mais fo...me
     F  C         Dm               C
E aqui vive tua igreja em torno a ti
     Bb          F     Gm           C4   C
Onde se encontrará     a morada eterna

Dm          C       F
Verbum caro factum est
        C           Dm
Verbum panis factum est
            C       F
Verbum caro factum est
        Gm Am
Verbum panis

Dm           C
Desde o princípio
         Dm        C         Dm        C
Quando o universo foi criado da escuridão
Dm         C             Dm C Dm C
O Verbo estava junto a Deus
Dm       C
Veio no mundo
     Dm        C              Dm         C
Rico em misericórdia Deus mandou o filho seu
Dm         C         Dm C
Todo a si mesmo como pão

Dm          C        F
Verbum caro factum est
        C           Dm
Verbum panis factum est
            C       F
Verbum caro factum est
        C           Bb      C
Verbum panis factum est

     F    C         Dm             C
E aqui partes o teu pão em meio a nós
      Bb          F    Gm            C4   C
Todo aquele que comer  não terá mais fo...me
     F  C         Dm               C
E aqui vive tua igreja em torno a ti
     Bb          F     Gm           C4   C
Onde se encontrará     a morada eterna

     F    C         Dm             C
E aqui partes o teu pão em meio a nós
      Bb          F    Gm            C4   C
Todo aquele que comer  não terá mais fo...me
     F  C         Dm               C
E aqui vive tua igreja em torno a ti
     Bb          F     Gm           C4   C
Onde se encontrará     a morada eterna

Dm          C       F
Verbum caro factum est
        C           Dm
Verbum panis factum est
            C       F
Verbum caro factum est
         Am Dm
Verbum panis"""
# print(musica.split())
print(Counter(musica.split()))
res = Counter(musica.split())
print(res.most_common(5))   # Método para encontrar as palavras mais comuns no testo

teste = "Ainda é cedo!"
print(Counter(teste.split()))