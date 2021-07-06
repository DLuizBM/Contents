
class Pessoa:
    def __init__(self, nome, altura, idade):
        self.__nome = nome
        self.__altura = altura
        self.__idade = idade

    def getname(self):
        return self.__nome

    def getheight(self):
        return self.__altura

    def getage(self):
        return self.__idade

    def getdata(self):
        return f'A/O {self.__nome} tem {self.__altura} metros de altura e {self.__idade} de idade.'


pessoa1 = Pessoa('Hamilton', '1,63', '33')
pessoa2 = Pessoa('Vettel', '170', '31')

print(pessoa2.getname())
print(pessoa1.getdata())



