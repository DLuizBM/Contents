"""
Pacotes

Módulos -> é um arquivo python que pode ter diversas função para utilizarmos
Pacote -> é um diretório contendo uma coleção de módulos

Ex: guppe é um pacote e os arquivos criados (ex: 61-map) são os módulos
OBS: nas versões 2.X do python, um pacote deveria conter dentro dele
um arquivo __init__.py
Nas versões 3.x isso não é mais necessário, porém ainda é utilizado normalmente
para manter compatibilidade

"""

# utilizando os pacotes
from MyPackage import módulo_1
print(módulo_1.func1(4, 5))
print(módulo_1.const)
# estou buscando o pacote MyPackage e importando o módulo_1, dentro de módulo_1
# estou utilizando a função func1, como mostrado no print. Além disso estou pegando
# o valor da variável const

from MyPackage import módulo_2
print(módulo_2.func2())

# Acessando subpcotes
from MyPackage.package2 import módulo_3, módulo_4
# passo o pacote principal.subpacote
print(módulo_3.fun3())
print(módulo_4.func4())

from MyPackage.package2.módulo_3 import fun3
print('Nós tamos em ' + fun3())

from MyPackage.módulo_2 import func2
print('Eu amo ' + func2())
