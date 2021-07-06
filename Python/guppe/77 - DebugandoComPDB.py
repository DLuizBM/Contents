"""
Debugando com PDB
PDB - Python Debugger

- Uma das formas de debugar é usar print, para ver valores das variáveis, mas essa
é uma prática ruim.


# Pycharm
def divisao(a, b):
    try:
        return a / b
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorre um erro: {err}'


print(divisao(3, 4))
# Para fazer o debugger no pycharm, basta colocar os pontos de início e fim
# apertar o símbolo de bug(inseto) e fazer  análise


# PDB
# deve-se importar a biblioteca pdb e então utilizar a função set_trace()

# comandos básicos de pdb
# l -> lista onde estamos no código
# n -> próxima linha
# p -> imprime variável
# c -> continua a execução/finaliza o programa


import pdb

nome = 'Lionel'
sobrenome = 'Messi'
import pdb; pdb.set_trace() # desas forma não é necesário declarar a biblioteca no início do programa
nome_completo = nome + ' Andrés ' + sobrenome
time = nome_completo + ' joga no Barcelona'
print(time)


# PDB
# deve-se importar a biblioteca pdb e então utilizar a função set_trace()
# A partir do python 3.7 não é mais necessário importar a biblioteca pdb, pois o comando
# debugger foi incorporado como função built-in chamada breakpoint()

# comandos básicos de pdb
# l -> lista onde estamos no código
# n -> próxima linha
# p -> imprime variável
# c -> continua a execução/finaliza o programa


import pdb

nome = 'Lionel'
sobrenome = 'Messi'
breakpoint()
nome_completo = nome + ' Andrés ' + sobrenome
time = nome_completo + ' joga no Barcelona'
print(time)
"""
# tomar cuidado com os conflitos entre nome de variável e os comandos do pdb

l = 1
c = 2
p = 3
n = 4
breakpoint()

print(l + c + p + n)
# imprimir a variável, deve-se colocar o comando p e em seguida a variável
# ex: se quisermos a variável p -> p p
# e a variável p seria impressa

