# Controlando a classe televisão pela classe controle remoto
# trabalhando diferente de herança


class Televisao:
    maxCanal = 200
    maxVol = 100

    def __init__(self):
        self.__canal = 0
        self.__volume = 0
        self.__ligada = False

    @property
    def imprimir(self):
        return f'Canal:{self.__canal}\nVolume:{self.__volume}\nLigada: {self.__ligada}'

    def __ligar(self, valor):
        self.__ligada = valor

    def aumentar_canal(self, valor):
        if self.__canal < Televisao.maxCanal:
            self.__canal += valor
        elif self.__canal == Televisao.maxCanal:
            self.__canal = 1

    def abaixar_canal(self, valor):
        if self.__canal > 1:
            self.__canal -= valor
        elif self.__canal == 1:
            self.__canal = Televisao.maxCanal

    def aumentar_volume(self, valor):
        if self.__volume < Televisao.maxVol:
            self.__volume += valor

    def abaixar_volume(self, valor):
        if self.__volume > 0:
            self.__volume -= valor


class ControleRemoto:
    def __init__(self, televisao):
        self.__televisao = televisao

    def informacoes(self):
        return self.__televisao.imprimir

    def liga(self, valor):
        self.__televisao._Televisao__ligar(valor)
        # pode ter return ou não
        # _Televisao__ligar(valor), pois o métofo ligar em Televisão é privado

    def aumenta_canal(self):
        self.__televisao.aumentar_canal(1)

    def abaixa_canal(self):
        self.__televisao.abaixar_canal(1)

    def volume_acima(self):
        self.__televisao.aumentar_volume(1)

    def volume_abaixo(self):
        self.__televisao.abaixar_volume(1)


tv = Televisao()
cr = ControleRemoto(tv)
cr.liga(True)
cr.aumenta_canal()
cr.aumenta_canal()
cr.aumenta_canal()
cr.abaixa_canal()
cr.volume_acima()
cr.volume_acima()
cr.volume_abaixo()
cr.volume_abaixo()
cr.volume_abaixo()
print(cr.informacoes())

