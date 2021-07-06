"""
Forçando tipos de dados com decoradores



# Forçando tipos

a = (str, int, float, str)
arg = ('geek', '1', '2', 4.5)
novo = []

for (valor, tipo) in zip(arg, a):    # zip(arg, a) -> (str, geek), (int, '1'), (float, '2'), (str, 4.5)
    print(valor)                     # como são 4 tuplas, serão 4 loops, em cada loop valor e tipo recebem os valores
    print(tipo)                      # da tupla correspondente
    novo.append(tipo(valor))

print(novo)



def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo = []
            for (valor, tipo) in zip(args, tipos):
                novo.append(tipo(valor))
                print(novo)
            return funcao(*novo, **kwargs)
        return converte
    return decorador


@forca_tipo(float, float)
def divide(a, b):
    return a / b


print(divide('3', '2'))



def soma(funcao):
    def arg(*args, **kwargs):
            vet = [] # sempre executar o que se deseja fazer logo após a função que pega os parâmetros
            for num in args:
                vet.append(num + 100)
            return funcao(*vet, **kwargs)
    return arg

@soma
def mostra(n1, n2):
    return f'Numero: {n1+n2}'

print(mostra(5, 10))



def cria_lista(funcao):
    def arg(*args, **kwargs):
        vet = []
        for n in range(1, args[0] + 1):
            vet.append(n)
        return funcao(*vet, **kwargs)
    return arg

@cria_lista
def mostra(*a):
    return a

print(mostra(10))

"""


def decoradora(funcao):
    def pegaargumento(*args, **kwargs):
        vet = []
        for n in args:
            vet.append(n+10)
        return funcao(*vet)
    return pegaargumento


@decoradora
def soma(*vet):
    return vet[0] + vet[1]


print(soma(5, 10))
