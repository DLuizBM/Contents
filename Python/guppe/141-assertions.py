"""
Assertions

Em python utilizamos a palavra assert para realizar simples afirmações
utilizadas nos testes

Utilizamos o assert em uma expressão que é válida ou não
Se a expressão for verdadeira, retorna none e caso seja falsa
levanta um erro do tipo AssertionError

OBS: podemos especificar, opcionalmente, um segundo argumento ou mesmo uma
mensagem de erro personalizada

OBS: a palavra assert, pode ser utilizada em qualquer função ou código nosso...
não precisa ser exclusivamente em teste

TDD - test driven development

OBS: deve-se tomar cuidado com o assert
se um programa for executado com -O, nenhum assert será executado
"""


def soma(a, b):
    assert a > 0 and b > 0, "Ambos precisam ser maior que 0"
    # se a > 0 e b > 0 return a + b, se não print "Ambos precisa..."
    return a + b


ret = soma(2, 3)
print(ret)


def comer(comida):
    assert comida in [
        'pizza',
        'sorvete'
    ], 'A comida deve ser fast food.'
    return f"Eu estou comendo {comida}"


print(comer("maçã"))














