"""
Definindo funções

Pequenos trechos de código que realizam tarefas específicas
- Pode ou não receber uma entrada de dados e retornar uma saída de dados
- Funções deve realizar tarefas simples, se uma função realiza muitas tarefa,
o ideal é que ela seja simplificada

Em python a forma geral de definir uma função é:

def nome_da_função(parâmetros de entrada):
    bloco_da_função

nome da função: sendo singular, tudo em minúsculo, se for plural os nomes devem ser separados por underline
parâmetros de entrada: Opcionais, onde tendo mais de um, cada um separado por vígula

# cores = ['azul', 'amarelo', 'verde', 'braco']

# utilizando a função integrada (Built-in) do python print()
# print(cores)

# Definando um função


def diz_oi():
    print("oi")

# OBS: Dentro de funções pode-se se chamar outras funções, no caso a função diz_oi
# também chama a função print
# essa função não recebe parâmetros e nem retorna nada

# Chamada de execução
diz_oi()    # Sempre colocar o parêntese para chamar a função


# Em python podemos inclusive criar variáveis do tipo de uma função e executar
# esta função através da variável

def diz_oi():
    print("oi oi oi oi")


diz = diz_oi    # A variável diz vai receber o que foi executado da função diz_oi
diz()

######################################################################################

FUNÇÕES COM RETORNO

OBS: Em python quando uma função não retorna valor, o retorno é NONE
OBS: Funções python que retornam valores, devem retornar valores com a palavra
reservada 'return'.
OBS: Não precisamos necessariamente criar uma variável para receber o retorna da função
Podemos passar a execução da função para outras funções

def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()   # Funções que tem retorno devem ser chamadas com o parênteses

print(ret)
print(quadrado_de_7() + 1)

OBS sobre o return
- Ela finaliza a função, ou seja, ela sai da execução da função:
- Podemos ter em uma função, diferentes returns
- Podemos em uma função, retornar qualquer tipo de dado, até mesmo multiplos valores


def diz_oi():
    print("Estou sendo executado depois do retun!")
    return 'OI!'
    print("Estou sendo executado depois do retun!")
    # Essa linha nunca será executada, pois está depois do return


print(diz_oi())


def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 5
    else:
        return 6
# A função possui vários returns, mas apenas um valor é retornado

print(nova_funcao())


def outra_funcao():
    return 1, 2, 3, 4


num1, num2, num3, num4 = outra_funcao()

print(f'{num1} {num2} {num3} {num4}')
print(outra_funcao())   # imprime no formato de tupla

OBS: Observar as codificações desnecessárias, por exemplo, excesso de if e else

##################################################################################

FUNÇÕES COM PARÂMETROS

- Funções que recebem dados para serem processados dentro da mesma.

Se pensarmos em funções, sabemos que existem funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada, mas não possuem saída;
- Possuem saída, mas não possuem entrada;
- Possuem entrada e saída.


def quadrado(numero):
    return numero ** 2


print(quadrado(7))
print(quadrado(23))
print(quadrado(198))



def soma(a, b):
    return a + b


def mensagem(c, d, msg):
    return (c + d) * msg


print(soma(5, 10))
print(soma(10, 20))

print(mensagem(1, 2, 'conseguiu '))
print(mensagem(4, 5, 'conseguiu de novo '))

# OBS: Se informarmos o número errado de parâmetros ou argumentos, o erro será TypeError

# Nomeando parâmetros para visualizar melhor o código


def nome_completo(nome, sobrenome):     # nome e sobrenome -- parâmetros
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Angelina', 'Jolie'))   # Angelina e Jolie -- argumentos

# Parâmentros são variáveis declaradas na definição da função
# Argumentos são dados passados durante a execução de uma função
# A ordem dos parâmetros importa

# Argumentos nomeados (keyword arguments)

print(nome_completo(nome='Brad', sobrenome='Pitt'))
print(nome_completo(sobrenome='Pitt', nome='Brad'))
# Nesse caso a ordem não mais importa, pois os argumentos foram nomeados, ou seja,
# O parâmetros foi nomeado

# Exemplo

def soma(numeros):
    tot = 0
    for num in numeros:
        tot = tot + num
    return tot


lista = [1, 3, 4, 5, 6, 7]
print(soma(lista))

#################################################################################

FUNÇÕES COM PARÂMETRO PADRÃO (DEFAULT PARAMETERS)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro é opcional

print('Olá')
print()

# Exemplo de função onde a passagem de parâmetro é obrigatória

def quadrado(num):
    return num ** 2


print(quadrado(3))
print(quadrado()) # TypeError

def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(5, 2))

# E se caso o usuário não informasse a potência e quiséssimos que o programa
# Elevasse o número a uma potência padrão

# Exemplo
print(exponencial(3))
# Para isso basta definir uma valor para a variável 'potencia' na definição da função, nesse caso 2
print(exponencial(3, 4))    # Caso seja passado o argumento, então a variável 'potencia' assumirá o valor do argumento

# Se os dois parâmetros na função fosse definidos como default, então a próxima
# Estrutura também funcionaria
print(exponencial())

OBS: Em função com parâmetros default, os parâmetros default devem sempre estar ao final
# exemplo
def quadrado(numero=2, potencia) # Errado
def quadrado(potencia, numero=2) # Certo


def mostra(nome='Geek', inst=False):
    if nome == 'Geek' and inst: # Colocando só 'inst' sem comparação, entende-se que a variável é verdadeira(True)
        return f'Olá instrutor!'
    elif nome == 'Geek':
        return f'Pensei que você era instrutor.'
    return f'Olá {nome}'


print(mostra())
print(mostra(inst=True))
print(mostra('Angelina'))

# Por que usar parâmetros default?
- Nos permite ser mais flexíveis nas funções
- Evita erros com parâmetros incorretos
- Nos permite trabalhar com exemplos mais legíveis no código
- Qualquer tipo de dado pode ser utilizado como valores default para parâmetros(até listas, tuplas, dicionários etc)



# Como passar função como parâmetro
def soma(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(mat(3, 3))        # Por default na função mat, vai fazer a soma
print(mat(3, 3, sub))   # Passando a função sub como parâmetro, para fazer a subtração



 # Escopo para evitar problemas e confusões

instrutor = 'Geek'  # variável global


def diz_oi():
    instrutor = 'python'    # variável local
    return f'Oi {instrutor}'


print(diz_oi())
# Em python a variável local se sobrepõe a global (quando ambas tem o mesmo nome)
# Variáveis locais são reconhecidas apenas no próprio bloco de execução

# Atenção: variáveis globais, se puder evitar, evite!

total = 0

def soma():
    total = total + 1 # UnboundLocalError, a variável total foi inicializada
                      # como 0, sendo variável global, mas ao iniciar definir
                      # total dentro da função e fazer total = total + 1, o python
                      # entende que ela não existe em (total + 1)
    return total

print(soma())


# Atenção: variáveis globais, se puder evitar, evite!

total = 0


def soma():
    global total
    total = total + 1 # UnboundLocalError, a variável total foi inicializada
                      # como 0, sendo variável global, mas ao iniciar definir
                      # total dentro da função e fazer total = total + 1, o python
                      # entende que ela não existe em (total + 1)
                      # para que funcione, deve-se colocar o global antes da variável
    return total


print(soma())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma
# especial de escopo de variável


def fora():
    contador = 40

    def dentro():
        nonlocal contador   # Define a variável como sendo a contador da função fora
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())
# print(dentro()) não é reconhecido

#####################################################################################
DOCSTRINGS
Documentando funções com docstrings


"""


def diz_oi():
    """ Função simples que retorna Oi!"""
    return f'Oi!'


diz = diz_oi # dessa forma, diz recebe apenas a funcão e não a execução dela
print(diz)
print(diz())
# No terminal python para ter acesso acesso a documentação da função
# from Definindo_funções import diz_oi
# Saída:Oi!
# >>> help(diz_oi)
# print(diz_oi.__doc__)
# Função simples que retorna Oi!


def exponencial(numero=1, potencia=1):
    """
    Função que gera a exponencial
    :param numero:
    :param potencia:
    :return:

    """
    return numero ** potencia
lista = [1, 2, 3, 4, 5 ,6, 'vim de Definindo_funções']

contador = 0
inicial = 5

def non_local():
    # inicial = inicial + 1
    # dessa forma, há problema, pois ao tentar ciar uma variável "inicial" e iniciando
    # ela com "inicial", a intencão é que fosse a global, mas o python entende que essa
    # é a incial que acabamos de criar, como ela não existe, há erro
    #contador = 10 + inicial
    # dessa forma, não há problema, pois estou criando uma outra variável, que é local,
    # e inciando ela com "inicial", o python entende que esse único inicial é o global
    # se necessário usar uma variável global de forma direta, basta chamá-la
    contador = 10
    global inicial # o global deve ser chamado para se trabalhar com a variável global, se essa
    # for sofrer algum processamente e seu valor tiver que ser mudado
    inicial = inicial + 100
    # a variável inicial que se está trabalhando é a global, logo, qualquer modificação feita nela
    # vai se refletir de forma global.
    # ao se fazer inicial = inicial + 100, não é criada uma variável local "inicial"

    def dentro():
        nonlocal contador
        contadores = contador + 1 + inicial  # inicial aqui é a global, por isso não é necessário colocar nonlocal
        return contadores
    return dentro()


print(f'valor inical antes da execução da função: {inicial}')
# valor de saída é 5
print("resultado: " + str(non_local()))
print(f'valor inical depois da execução da função: {inicial}')
# valor de saída é 105, pois durante a execução da função a variável global
# passa por um processamente e seu valor é alterado














































