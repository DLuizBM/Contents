"""
**kwargs
- Poderia se chamar esse parâmetro de qualquer nome
exemplo:
**xis

-Diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige
que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um
dicionário

def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor do/a {pessoa} é {cor}.')


cores(marcos='verde', paulo='azul', pedro='rosa')
# OBS: os parâmetros *args e **kwargs não são obrigatórios

# Exemplo 2


def cumprimento(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
    # Se a chave 'geek' está em kwargs e o valor de kwargs com essa chave for 'python'
        return f'Python geek!'
    elif 'geek' in kwargs:
        return f"Olá {kwargs['geek']}!"
    return f'Não sei quem é você.'


print(cumprimento())
print(cumprimento(geek='python'))
print(cumprimento(geek='C++'))

# Nas nossas funções podemos ter, nessa ordem:
-Parâmetros obrigatórios
-*args
-Parâmetros default(não obrigatórios)
-**kwargs


def minha_funcao(nome, idade, *args, solteiro=False, **kwargs):
    print(f'{nome}/{idade}.')
    print(args)
    if solteiro:
        print('Solteiro.')
    else:
        print('Casado.')
    print(kwargs)


minha_funcao('Divino', 24)
# Passando os parâmetros obrigatórios
print()
minha_funcao('Divino', 24, 'Engenheiro')
# Passando os parâmetros obrigatórios e *args
print()
minha_funcao('Divino', 24, 'Engenheiro', solteiro=True)
# Passando os parâmetros obrigatórios, *args e o parâmetro 'solteiro'
print()
minha_funcao('Divino', 24, 'Engenheiro', solteiro=True, sobrenome='Luiz', sobremone2='Barbosa')
# Passando os parâmetros obrigatórios, *args, o parâmetro 'solteiro' e o parêmetro
# **kwargs


# Desempacotamento com **kwargs


def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Ayrton', 'sobrenome': 'Senna'}
print(mostra_nome(**nomes)) # Duplo ** indica que deve ser feito o desempacotamento

"""


# Exemplo de desempacotamento


def soma(a, b, c, d=0, **kwargs):
    # desempacota em **kwargs e depois os valores(numéricos) são passado em ordem para a, b, e c
    # se houver uma chave valor, como Nome='Ayrton' e nome='Drailton', o python monta um diconário com esses valores
    print(a + b + c + d)
    if kwargs:
        print(f'{kwargs}')


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dic = dict(a=1, b=2, c=3, d=4, nome='Ayrton')
# OBS: Os nomes das chaves no dicionário devem ser o mesmo dos parâmetros na função

soma(*lista)
soma(*tupla)
soma(*conjunto)
soma(**dic, Nome='Drailton')










