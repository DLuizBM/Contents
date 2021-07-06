
class Equipamento:
    def __init__(self, preco, peso):
        self.__preco = preco
        self.__peso = peso

    @property
    def preco(self):
        return f'O preço é {self.__preco}'

    @property
    def peso(self):
        return self.__peso

    @preco.setter
    def preco(self, valor):
        self.__preco = valor

    @peso.setter
    def peso(self, valor):
        self.__peso = valor

    @property
    def exibe(self):
        return f'Preço:{self.__preco}.\nPeso:{self.__peso}'


class Computador(Equipamento):
    def __init__(self, preco, peso, hd, ram):
        super().__init__(preco, peso)
        self.__hd = hd
        self.__ram = ram

    @property
    def hd(self):
        return self.__hd

    @property
    def ram(self):
        return self.__hd

    @hd.setter
    def hd(self, valor):
        self.__hd = valor

    @ram.setter
    def ram(self, valor):
        self.__ram = valor

    # sobreescrevendo o método exibe
    @property
    def exibe(self):
        return f'Preço:{self._Equipamento__preco}.\nPeso:{self._Equipamento__peso}.\n' \
               f'HD:{self.__hd}.\nRAM:{self.__ram}.'
    # os atributos que são herdados da classe pai, preco e peso, devem ser chamados junto com a classe
    # self._Equipamento__preco, quando o método é sobreescrito


class TestaEquipamento:
    def __init__(self, equipamento, computador):
        self.__equipamento = equipamento
        self.__computador = computador

    def main(self):
        return f'Equipamento\n' \
                   f'Preço:{self.__equipamento.preco}\n' \
                   f'Peso:{self.__equipamento.peso}\n'\
                   f'Computador\n' \
                   f'Preço:{self.__computador.preco}\n' \
                   f'Peso:{self.__computador.peso}\n' \
                   f'HD:{self.__computador.hd}\n' \
                   f'RAM:{self.__computador.ram}\n'


desktop = Computador(3000, 25, 160, 8)
print(desktop.preco)
desktop.preco = 5000
print(desktop.preco)
print(desktop.exibe)

equip = Equipamento(2000, 3)
testa = TestaEquipamento(equip, desktop)
print(testa.main())




