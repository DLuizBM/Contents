
def potencia(x, z):
    tot = 1
    for _ in range(z):
        tot = tot * x
    print(f'{x} elevado a {z} é: {tot}')


X = int(input())
Z = int(input())
potencia(X, Z)