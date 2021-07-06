class Microondas:
    def __init__(self):
        self.__ligado = ''
        self.__porta = ''

    def __informacoes(self):
        return f'O microondas está:{self.__ligado}.\nA porta está:{self.__porta}'


class Mod(Microondas):
    def __init__(self):
        super().__init__()
        self._Microondas__ligado = ''
        self._Microondas__porta = ''

    def abre_porta(self):
        self._Microondas__porta = 'aberta'

    def fecha_porta(self):
        self._Microondas__porta = 'fechada'

    def liga(self):
        if self._Microondas__porta == 'fechada':
            self._Microondas__ligado = 'ligado'
        else:
            print(f'A porta está aberta!!')

    def desliga(self):
        self._Microondas__ligado = 'desligado'

    def infos(self):
        return super()._Microondas__informacoes()


micro = Mod()
micro.abre_porta()
micro.liga()
micro.fecha_porta()
micro.liga()
print(micro.infos())

