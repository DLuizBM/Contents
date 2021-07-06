"""
São módulos criados por nós mesmo.

# Fazendo import do arquivo Definindo_funções e utilizando a função diz_oi

from Definindo_funções import diz_oi
print(diz_oi())
# Imprime 2 Oi!, pois a chamada da função no arquivo Definindo_funções está dentro
# de um print e por isso tem o print dentro do arquivo e o print nesse arquivo

from Definindo_funções import exponencial
print(exponencial(2, 3))
# Chamada da função exponencial


import Definindo_funções as df
# importando dessa forma, temos acesso a todos os elementos do módulo
# inclusive variáveis

# exemplo, pegando a lista que está em Definindo_funções
print(df.lista)

"""
# importando de Map

from Map import cidades, celsius_f
# Importando de Map a variável cidades e função lambda celsius_f
# esse arquivo é o 61 - Map, mudar para Map para rodar o exemplo
print(list(map(celsius_f, cidades)))