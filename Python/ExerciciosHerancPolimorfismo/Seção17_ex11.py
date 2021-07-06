class Moto:
    def __init__(self, marca, modelo, motor):
        self.__marca = marca
        self.__modelo = modelo
        self.__motor = motor
        self.__marcha = 0

    def __informacoes(self, valor):
        return f'Marca:{self.__marca}.\nModelo:{self.__modelo}.\nMotor:{self.__motor}.\nMarcha:{self.__marcha}.' \
               f'\nValor passado: {valor}. '


class MudaInfo(Moto):
    def __init__(self, marca, modelo, motor):
        super().__init__(marca, modelo, motor)
        # self._Moto__marcha = 0
        # adicionar caso queira tirar a tarja amarela no método aumenta_marcha

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def motor(self):
        return self.__motor

    @property
    def marcha(self):
        return self.__marcha

    @marca.setter
    def marca(self, valor):
        self.marca = valor
        # self.moto, possível pois há um property para o atributo 'marca'
        # sem o property, deve colocar o dunder, self.__marca.

    @modelo.setter
    def modelo(self, valor):
        self.modelo = valor

    @motor.setter
    def motor(self, valor):
        self.motor = valor

    @property
    def moto(self):
        return super()._Moto__informacoes(3)
        # chamando o método informacoes e passando o valor 3, super()._Moto__informacoes(3)
        # está dessa forma, pois o método é privado, caso não fosse, super().informações(3)
        # importante notar que o método informacoes não pode estar com o o decorator @property
        # quando se passa argumentos, deve-se tirar o property

    def aumenta_marcha(self):
        self._Moto__marcha += 1
        # é possível chamar o atributo marcha dessa forma sem declarar no construtor
        # para sair a tarja amarela, basta declarar no construtor de MudaInfo

    def diminui_marcha(self):
        self._Moto__marcha -= 1


moto1 = MudaInfo('Honda', 'CG 2020', '150cc')
moto1.aumenta_marcha()
moto1.aumenta_marcha()
moto1.diminui_marcha()
moto1.aumenta_marcha()
moto1.aumenta_marcha()
print(moto1.moto)