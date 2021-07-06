"""
Funções de maior grandeza - Higher Order Functions - HOF

O que isso significa?
- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
que retornam outras funções como resultado, ou mesmo que podemos passar funções
como argumentos e até mesmo criar variáveis do tipo de funções nos nossos programas

OBS: Na seção de funções, usamos isso

Em python as funções são cidadões de primeira classe

# Exemplo


def soma(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def calcula(n1, n2, funcao):    # recebendo uma função como parâmetro
    return funcao(n1, n2)


print(calcula(10, 5, soma))
print(calcula(10, 5, sub))
print(calcula(10, 5, mult))
print(calcula(10, 5, div))


Nested function - funções aninhadas
- Em python também podemos ter funções dentro de funções. Que são conhecidas por Neste Functions
ou também por inner functions (funções internas)


# Exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(['Eai', 'Suma daqui', 'Gosto de você'])
    return humor() + ' ' + pessoa

print(cumprimento('Ayrton'))
print(cumprimento('Hamilton'))


from random import choice

def faz_rir():
    def rir():
        return choice(('hahahahahaha', 'rsrsrssrsrssr', 'kkkkkkkkkk'))
    return rir
    # importante notar que, o return dessa forma significa que o que está sendo retornado
    # é a função e não a execução da função ou seja, não está retornando nenhum valor
    # diferente de return rir(), que vai retornar a execução da função

rindo = faz_rir()
# foi colocado na variável rindo o retorno de faz_rir(), ou seja, foi colocado na variável
# rindo a função rir
print(rindo())
# rindo() executa a função rir()


OBS: Inner functions/Nested functions podem acessar o escopo de funções mais externas
"""
# Exemplo

from random import choice

def faz_rir(pessoa):
    def dando_risada():
        risada = choice(('hahahhaha', 'kkkkkkkkk', 'rsrsrsrsrs'))
        return f'{risada} {pessoa}'
        # importante notar que a função dando_risada() está tento acesso a 'pessoa' que é um parâmetro
        # da função mais externa faz_rir
    return dando_risada
    # retornando a função e não a execução da função

rindo = faz_rir('Ayrton')
print(rindo())