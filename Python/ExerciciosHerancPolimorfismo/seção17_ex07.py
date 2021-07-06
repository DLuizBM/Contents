class Circulo:
    def __init__(self):
        self.__raio = 0
        self.__area = 0
        self.__perimetro = 0

    def __calculaarea(self):
        self.__area = 3.14 * self.__raio ** 2
        return self.__area.__round__(3)
        # retornando com 2 casas decimais

    def __calculaperimetro(self):
        self.__perimetro = 2 * 3.14 * self.__raio
        return self.__perimetro.__round__(2)
        # retornando com 2 casas decimais

    @property
    def area(self):
        return self.__calculaarea()

    @property
    def perimetro(self):
        return self.__calculaperimetro()

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, valor):
        self.__raio = valor


bola = Circulo()
bola.raio = 10.2
print(bola.area)
print(bola.perimetro)
