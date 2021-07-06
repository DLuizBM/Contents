"""
LAMBDAS
São funções sem nomes, anôminas
Aplicadas para fazer filtragem e ordenação de dados

def funcao(x):
    return 3 * x + 1


print(funcao(3))


# Função lambda

lambda x: 3 * x + 1
#recebe x : e retorna 3 * x + 1(: sepera o que recebe do que retorna)

# Como utilizar? Método não "correto"

cal = lambda x: 3 * x + 1
print(cal(3))

# Lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# strip(), retira os espaços ' ' no início e no fim da variável
# title(), converte toda string em minúsculo e deixa apenas a inicias em maiúsculo
print(nome_completo("divino  ", "Luiz"))


# Assim como nas funções normais, lambda pode ter nenhuma, uma ou várias entradas

ex1 = lambda: "Eu amo programar."
ex2 = lambda x: x + 100
ex3 = lambda x, y, z: x + y + z

print(ex1())
print(ex2(10))
print(ex3(10, 20, 30))

# Se passarmos mais ou menos parâmetros para a função, TypeError
lista = ['Nigel Mansell', 'Michael Schumacher', 'Fernando Alonso', 'Ayrton Senna', 'Lewis Hamilton', 'Sebastien Vettel']

# Organizando uma lista de nomes pelo sobrenome
lista.sort(key=lambda sobrenome: sobrenome.split()[-1])
# Sort pode ser organizado por uma chave(key)
# o que a função faz é pegar o sobrenome(variável 'sobrenome' na função) na posição [-1]
# lembrado que em listas é possível fazer isso, pois assim tem-se a certeza de estar pegando
# a última posição da string, que é o sobrenome
print(lista)


"""

# Cálculo função quadrada

def funcao_quadrada(a, b, c):
    return lambda x: a*x**2 + b*x + c

funcao = funcao_quadrada(1, 2, 3)
# passando os valores de a, b e c
print(funcao(2))
print(funcao(3))
print(funcao(4))
# passando valores para x
# Nesse caso existem dois processos para passar valores para a função
# 1 - valores de a, b e c
# 2 - valor de x

lista = ['Nigel Mansell', 'Michael Schumacher', 'Fernando Alonso', 'Ayrton Senna', 'Lewis Hamilton', 'Sebastien Vettel']
lista.sort(key=lambda sobrenome: sobrenome.split(' ')[-1], reverse=False)
print(lista)





