"""
Dunder Name e Dunder main

Dunder Name: __name__
Dunder Main: __main__

Em python são utilizados dunder para criar funções, atributos, propriedades, e etc
utilizando Duble under para não gerar conflito com os nomes desses elementos na programação

- Em python se executarmos um módulo python diretamente na linha de comando, internamente
o python atribuirá a variável __name__ o valor __main__ indicando que este é o módulo de
execução principal
"""
import primeiro
import segundo
# Nessa linha como o módulo ainda não foi executado, __name__ não recebe __main__, dessa forma
# a saída será:
# Primeiro foi importado.
# Segundo foi importado

