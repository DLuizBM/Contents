class Moto:
    def __init__(self):
        self.__marca = 'Honda'
        self.__modelo = 'CG 2020'
        self.__motor = 0
        self.__marcha = 0

    @property
    def mostramotor(self):
        return self.__motor

    @property
    def mostramarcha(self):
        return self.__marcha

    @property
    def infos(self):
        return f'A marca da moto é: {self.__marca}.\nO modelo é: {self.__modelo}.\nA moto está na marcha: {self.__marcha}.\nA moto possui motor: {self.__motor}.'


class MudaMarchaMotor(Moto):
    def __init__(self):
        super().__init__()
        self._Moto__marcha = 0
        self._Moto__motor = 0
        # self._classe__atributo = valor
        # para acessar o atributo marcha (por herança) da classe Moto, quando esse
        # não está definido no construtor de Moto. O mesmo serve para o atributo motor

    @property
    def mudamarcha(self):
        return self._Moto__marcha

    @mudamarcha.setter
    def mudamarcha(self, valor):
        self._Moto__marcha = valor
        # mudando o valor do atributo marcha que está na classe Moto

    @property
    def muda_motor(self):
        return self._Moto__motor

    @muda_motor.setter
    def muda_motor(self, valor):
        self._Moto__motor = valor
        # mudando o valor do atributo motor que está na classe Moto

    @property
    def mostrainfos(self):
        return super().infos
        # acesso a método de outra classe (por herança) -> super().método
        # acessando o método infos()(parênteses se infos não tivesse o property) da classe Moto
        # pelo método mostrainfos da classe
        # MudaMarcha


r1 = MudaMarchaMotor()
r1.mudamarcha = 'Neutro'
r1.muda_motor = '150cc'
print(r1.mostramarcha)
print(r1.mostramotor)
print(r1.mostrainfos)




