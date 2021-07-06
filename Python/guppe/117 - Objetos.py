"""
Objetos/instância: São instâncias da classe
- Para criar um objeto deve-se passar os parâmetros que ele espera no construtor

- Acessando atributos e métodos de uma classe, dentro de outra classe
self.objeto._Classe(que quero acessar)__atributo
self.objeto.método(que quero acessar)
"""

"""
class Carro:

    def __init__(self, modelo, motor, acabamento):
        self.__modelo = modelo
        self.__motor = motor
        self.__acabamento = acabamento
        self.__disponivel = True

    def disponivel_estoque(self):
        if self.__disponivel:
            self.__disponivel = False
        else:
            self.__disponivel = True

    def checa_estoque(self):
        return self.__disponivel

    def get_car_model(self):
        return self.__modelo


class Concessionaria:
    def __init__(self, nome, local, carro):
        self.__nome = nome
        self.__local = local
        self.__carro = carro

    def mostra_carro(self):
        return f'O carro que temos na concessionária é: {self.__carro.get_car_model()}'  # forma correta de acesso
        # return f'O carro que temos na concessionária é: {self.__carro._Carro__modelo}'
        # não existe atributo privado em python, o que existe é uma conveção para indicar que atributos e
        # métodos não fazem parte da api pública, isso é contornado com o name mangling
        # quando se passa um objeto como parâmetro, é possível ter acesso a métodos e atributos da classe de
        # de onde este objeto está vindo. O objeto traz tudo, classe, métodos e atributos


carro1 = Carro('Civic', '1.5 Turbo', 'soft-touch')
carro2 = Carro('Corolla', '2.0', 'soft-touch')

print(carro1.checa_estoque())
carro1.disponivel_estoque()     # toda vez que executo o método o valor muda
print(carro1.checa_estoque())
carro1.disponivel_estoque()
print(carro1.checa_estoque())

#################################################################################

conc = Concessionaria('Saga Toyota', 'Subida do Colorado', carro2)
# passando um objeto como parâmetro para outra classe
print(conc.mostra_carro())

"""