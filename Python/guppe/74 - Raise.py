"""
Levantando os próprios erros com o raise

raise -> lança execessões, é útil para criar nosssas excessões e msg's de erros.
OBS: Não é uma funçõa, é uma palavra reservada

A forma geral de utilização é:

raise TipoDoErro("mensagem de erro")

# Exemplo

def colore(texto.txt, cor):
    if type(texto.txt) is not str:
        raise TypeError("O texto.txt precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("A cor precisa ser uma string")
    else:
        print(f'O texto.txt {texto.txt} será impresso na cor {cor}.')

colore(2, 1)

def colore(texto.txt, cor):
    cores = ('azul', 'amarelo', 'verde')
    if type(texto.txt) is not str:
        raise TypeError("O texto.txt precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("A cor precisa ser uma string")
    if cor not in cores:
        raise ValueError(f"A cor não está in {cores}, precisa estar.")
    else:
        print(f'O texto.txt {texto.txt} será impresso na cor {cor}.')

colore("Cordel", "Preto".lower())
# lower() faz todas as letras passarem para minúsculo

# OBS: O raise assim como o return, finaliza a função; Ou seja, nada após raise
é executado.

"""

