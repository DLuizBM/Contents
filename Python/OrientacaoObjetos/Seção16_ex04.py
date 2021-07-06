pclass Televisao:
    canais = 30
    volume = 0

    def __init__(self):
        self.__canal = 0
        self.__volume = Televisao.volume
        self.__teste = 1000
        # nos métodos que envolvem canais, foi usado diretamente self.__canal para aumentar e diminuir (mais indicado de
        # fazer) e o atributo canais para funcionar como um controle limitador
        # já nos métodos que envolvem volumes, foi usado o atributo de classe(volume) para fazer os cálculos e depois
        # passar para self.volume

    def aumenta_canal(self, valor=1):
        if Televisao.canais > self.__canal >= 0:
            self.__canal = valor
            self.pega_canal()
        else:
            print('Este é o canal máximo')

    def diminui_canal(self, valor=1):
        if self.__canal >= 0 and self.__canal - valor >= 0:
            self.__canal -= valor
            self.pega_canal()
        else:
            print(f'Não é possível abaixar mais os canais.')
            print('')

    def pega_canal(self):
        print(f'Canal {self.__canal}')

    def aumenta_volume(self, valor):
        Televisao.volume += valor
        self.__volume = Televisao.volume
        self.pega_volume()  # forma para acessar um método dentro de outro método

    def diminui_volume(self, valor):
        if Televisao.volume > 0:
            Televisao.volume -= valor
            self.__volume = Televisao.volume
            self.pega_volume()
        else:
            print('O volume está no mínimo.')

    def pega_volume(self):
        print(f'Volume {self.volume}')


class ControleRemoto:

    def __init__(self, televisao):
        self.__televisao = televisao

    def diminui_canal(self, valor=1):
        # print(self.__televisao._Televisao__canal) self.__televisao._Televisao__canal, acesso ao atributo
        self.__televisao.diminui_canal(valor)  # modo de se fazer acesso à métodos de outra classe
        # print(self.__televisao.canal), essa forma de acessa também é possível
        # porém somente quando o atributo é de classe(como canal e volume,como o teste é de instância,com ele n/funcion)

    def aumenta_canal(self, valor=1):
        self.__televisao.aumenta_canal(valor)

    def diminui_volume(self, valor=1):
        self.__televisao.diminui_volume(valor)

    def aumenta_volume(self, valor=1):
        self.__televisao.aumenta_volume(valor)


tv1 = Televisao()
cr1 = ControleRemoto(tv1)
cr1.aumenta_canal(30)
cr1.aumenta_canal()
cr1.diminui_canal(30)
cr1.diminui_canal()
cr1.aumenta_volume(100)
cr1.diminui_volume(50)

