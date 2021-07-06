"""
Try / except / else / finally
- Quando e onde tratar um erro?
- Toda entrada do usuário/ de dados deve ser tratada!!!!
OBS: A função do usuário é destruir seu sistema

# Exemplo de entrada de valor errado
num = 'um valor inválido'
try:
    num = int(input('Digite um número: '))
except ValueError:
    print('Valor incorreto!')
print(f'Você digitou {num}.')
# Ainda assim será apresentado erro, pois mesmo o erro sendo tratado, ele vai tentar
# imprimir num, e num, caso gere erro, não será criada
# para que isso não ocorra, num pode ser declarado com um valor para que não apresente erro


# Else -> executado somente se não houver erro
try:
    num = int(input('Digite um número: '))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'Você digitou {num}.')

# tente (execução), caso dê erro imprima 'valor incorreto!', se não der erro imprima
# 'você digitou {num}'

# Finally

try:
    num = int(input('Digite um número: '))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'Você digitou {num}.')
finally:
    print('Executando o finally.')
# O finally é executado independete de erro ou não
# Finally geralmente utilizado para fechar ou desalocar recursos


# Exemplo mais complexo - tratamento de forma errada


def divisao(a, b):
    return a/b


num1 = int(input('Entre com um valor: '))
try:
    num2 = int(input('Entre com um valor: '))
except ValueError:
    print('Valor errado!')

try:
    print(divisao(num1, num2))
except NameError:
    print('Variável não declarada.')

# num 1 também deveria ser tratado
# tratando dessa forma o código fica ruim de ser ler, essa é uma forma incorreta
# de se tratar erros


# Exemplo mais complexo - tratamento de forma correta
# OBS: Você é responsável pelas funções

def divisao(a, b):
    try:
        return int(a)/int(b)
    except ValueError:
        return f'Valor digitado está incorreto.'
    except ZeroDivisionError:
        return f'Não é possível fazer divisão por zero.'


num1 = input('Entre com um valor: ')
num2 = input('Entre com um valor: ')
# recebendo string e fazendo a conversão somente na função, dessa forma é possível
# receber qualquer tipo de dado, e trabalhar com ele somente dentro da função, trabalhando
# só lá também o tratamento de erros.

print(divisao(num1, num2))
# Possível fazer de forma genérica, não é o correto

"""
# Forma semigenérica


def divisao(a, b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}.'
        # com err, a mensagem de erro vai vir automaticament de acordo com o problema que o python
        # identificar. Se for ValueError, a msg de ValueError, ZeroDivisionError, a sua msg.


num1 = input('Entre com um valor: ')
num2 = input('Entre com um valor: ')

print(divisao(num1, num2))