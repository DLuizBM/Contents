"""
Preservando metadata com wraps

Metadata-> são dados intrínsecos em arquivos.

Wraps -> são funções que envolvem elementos com diversas finalidades

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        ""Eu sou uma função (logar)dentro da outra""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(n1, n2):
    ""Soma 2 números "" aspas triplas, aspas duplas aqui só para não dar erro
    return n1 + n2


print(soma(10, 20))

print(soma.__name__)
# Saída: logar
print(soma.__doc__)
# Saída: Eu sou uma função (logar)dentro da outra

# Saídas estão incorretas, pois deveria sair o nome da função soma e sua documentação e não a de logar
# o decorator está fazendo essa alteração

"""

# Problema Resolvido

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar)dentro da outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(n1, n2):
    """Soma 2 números """
    return n1 + n2


print(soma(10, 20))
print(soma.__name__)
print(soma.__doc__)
# isso é importante para criar uma boa documentação de bibliotecas, por exemplo