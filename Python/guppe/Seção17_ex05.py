class Retangulo:
    def __init__(self):
        self.__comprimento = 0
        self.__largura = 0
        self.__area = 0
        self.__perimetro = 0

    @property
    def comprimento(self):
        return self.__comprimento

    @property
    def largura(self):
        return self.__largura

    @comprimento.setter
    def comprimento(self, novo_comprimento):
        self.__comprimento = novo_comprimento

    @largura.setter
    def largura(self, nova_largura):
        self.__largura = nova_largura

    def __calcula_area(self):
        self.__area = self.largura * self.comprimento
        return self.__area

    def __calcula_perimetro(self):
        self.__perimetro = 2 * self.largura + 2 * self.comprimento
        return self.__perimetro

    @property
    def mostra(self):
        return f'Área: {self.__calcula_area()}.\nPerímetro: {self.__calcula_perimetro()}.'


retangulo = Retangulo()
retangulo.comprimento = 5
retangulo.largura = 4
print(retangulo.comprimento)
print(retangulo.mostra)

