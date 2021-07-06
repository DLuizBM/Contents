"""
Doctests: são testes que rodamos nas docstrings do python
para rodar um doctest: python -m doctest -v nome_do_programa.py

Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    143 - Doctests
1 items passed all tests:
   1 tests in 143 - Doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.



# para rodar o programa corretamente deve-se fazer
# python nome_programa.py
# é feito para rodar programas que tem testes
# se for feito o run direto da ide, apresenta erro


def soma(a, b):
    botar as docstrings
    #Retorna a soma de a mais b
    #:param a:
    #:param b:
    #:return:

    #>>> soma(1, 2) # vai fazer esse teste, 3 é colocado propositalmente, pois é a saída esperada, se colocar 4, o teste vai falhar
    #3

    #>>> soma(4, 6) # 10 é a saída esperada
    #10



    return a + b
print(soma(3, 4))



def duplicar(valores):


    :param valores:
    :return:

    #>>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    #>>> duplicar([])
    []

    #>>> duplicar(['a', 'b', 'c', 'd'])
    ['aa', 'bb', 'cc', 'dd']

    #>>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    return [2 * element for element in valores]
"""


def fala_oi():
    """
    :return:
    >>> fala_oi()
    "oi"

    """
    # por conta das aspas tripla
    # aspas dupla não é reconhecida
    # sendo assim, se o teste for executado, será apresentado erro
    # para que seja correto, deve-se trocar aspas dupla por ''
    return "oi"


print(fala_oi())


def verdade():
    """

    :return:

    >>> verdade()
    True
    """
    return True
# esse teste em algum editor de texto e rodando no terminal, pode falhar
# isso porque no teste se escrevermos True e dar espaço
# o teste vai esperar True mais os espaços
# o retorno da função não retorna os espaços, isso pode ocasionar erro
# o pycharm elemina os espaços após o True(linha 92)
# por isso, aqui sempre funciona




