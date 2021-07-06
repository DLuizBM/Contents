"""
Decorators com diferentes assinaturas


# relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

# teste
print(saudacao('Hamilton'))


# Decorator patterns
# Usando quando se tem mais de um argumento passado para o decorador

def gritar(funcao):
    def aumentar(*args, **kwargs): # dessa forma, podemos passar nenhum, um ou vários parâmetros
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Gostaria de pedir {principal} e {acompanhamento} de acompanhamento'

# Teste
print(saudacao('Hamilton'))
print(ordenar('picanha', 'arroz'))

# Podemos nomear os parâmetros
print(ordenar(principal='Filé mignon', acompanhamento='feijão'))

"""
# Decorator com argumentos


def verifica_primeiro_argumento(valor):     # valor recebe o parâmetro estabelecido quando se chama o decorador
    def interna(funcao):                    # recebe a função em questão (no caso, soma)
        def outra(*args, **kwargs):         # def outra é necessária para pegar os parâmetros dessa função
            print(*args)
            if args[0] != valor:
                return f'Valor incorreto! O primeiro argumento deve ser {valor}'
            return funcao(*args, **kwargs)   # se estiver tudo certo, retorna a função executada
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma(n1, n2):
    return n1 + n2


print(soma(10, 20))

