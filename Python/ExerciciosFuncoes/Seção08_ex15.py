
def verifica_triangulo(a, b, c):
    if (a < b + c) and (b < c + a) and (c < a + b):
        tipo_triangulo(a, b, c)


def tipo_triangulo(a, b, c):
    if a == b == c:
        print(f'Triângulo equilátero!')
    elif (a == b != c) or (a == c != b) or (b == c != a):
        print(f'Triângulo isóceles!')
    else:
        print(f'Triângulo escaleno!')


a = int(input())
b = int(input())
c = int(input())

verifica_triangulo(a, b, c)