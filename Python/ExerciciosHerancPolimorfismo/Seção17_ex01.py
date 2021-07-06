class Quadrado:
    def __init__(self, lado):
        self.__area = 0
        self.__lado = lado
        self.__perimetro = 0

    def __calcula_area(self):   # métodos privados
        self.__area = self.__lado ** 2
        return self.__area

    def __calcula_perimetro(self):
        self.__perimetro = self.__lado * 4
        return self.__perimetro

    def mostra(self):
        return f'Área: {self.__calcula_area()}\nPerímetro: {self.__calcula_perimetro()}'
        # self.__calcula_area() -> chamando o método privado


quadrado = Quadrado(2)
print(quadrado.mostra())
print(quadrado._Quadrado__calcula_perimetro())

# como o método é privado, essa a forma de chamar o método, mas não o ideal
# o método mostra(), já busca as informações dos métodos privados

