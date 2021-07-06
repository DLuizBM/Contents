class Moto:
    def __init__(self, marca, modelo, motor, marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__motor = motor
        self.__marcha = marcha

    @property
    def informacoes(self):
        return f'Marca:{self.__marca}.\nModelo:{self.__modelo}.\nMotor:{self.__motor}.\nMarcha:{self.__marcha}'


class MudaInfo(Moto):
    def __init__(self, marca, modelo, motor, marcha):
        super().__init__(marca, modelo, motor, marcha)

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

    @marcha.setter
    def marcha(self, valor):
        self.marcha = valor

    @property
    def moto(self):
        return super().informacoes


moto1 = MudaInfo('Honda', 'CG 2020', '150cc', 'Neutro')
print(moto1.moto)