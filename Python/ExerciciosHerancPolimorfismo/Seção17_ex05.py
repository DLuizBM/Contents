class Retangulo:

    def __init__(self):
        self.__cumprimento = 0
        self.__largura = 0
        self.__area = 0
        self.__perimetro = 0

    @property
    def area(self):
        return self.__calculaarea()

    @property
    def perimetro(self):
        return self.__calculaperimetro()

    @property
    def largura(self):
        return self.__largura

    @property
    def cumprimento(self):
        return self.__perimetro

    @largura.setter
    def largura(self, valor):
        self.__largura = valor
    # para usar o @property.setter, o @property deve estar definido
    # @largura.setter definido após o @property de largura

    @cumprimento.setter
    def cumprimento(self, valor):
        self.__cumprimento = valor

    def __calculaarea(self):
        self.__area = self.__cumprimento * self.__largura
        return self.__area

    def __calculaperimetro(self):
        self.__perimetro = 2 * (self.__cumprimento + self.__largura)
        return self.__perimetro


retangulo = Retangulo()
retangulo.largura = 30
retangulo.cumprimento = 30
print(retangulo.area)
print(retangulo.perimetro)
print(retangulo._Retangulo__calculaperimetro())
# acessando o método privado, prática não recomendável