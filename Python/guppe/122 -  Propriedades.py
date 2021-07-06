"""
POO - Propriedades

Em linguagens como o java, ao declararmos atributos privados nas classes, costumamos
criar métodos públicos para a manipulação desses atributos. Esses métodos são conhecidos
como getters e setter, onde o getter retorna o valor do atributo e o setter altera o valor do mesmo


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__conta = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__conta

    def extrato(self):
        return f'Saldo: {self.__saldo}\nTitular: {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.__saldo += valor

    def get_titular(self):
        return f'{self.__titular}'

    def get_limite(self):
        return f'{self.__limite}'

    def set_limite(self, limite):   # setters são perigosos, deve-se pensar bem antes de usar setters
        self.__limite = limite


c1 = Conta('Hamilton', '15000', '20000')
print(c1.extrato())
print(c1.get_limite())
c1.set_limite(200000)
print(c1.get_limite())

# Refatorando a classe anterior usando properties


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__conta = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__conta

    def extrato(self):
        return f'Saldo: {self.__saldo}\nTitular: {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.__saldo += valor

    @property
    def conta(self):
        return self.__conta

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter  # setter no 'formato de propriedade'
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def acesso_saldo(self):
        return self.__saldo

    @property
    def valor_total(self):
        # return self.limite + self.saldo dessa forma é possível pois existem as properties saldo e limite
        return self.__saldo + self.__limite


c1 = Conta('Hamilton', 15000, 20000)
print(c1.saldo)     # chamando a propriedade saldo
print(c1.acesso_saldo())    # chamando o método acesso_saldo
# o métodos acesso_saldo faz o mesmo que a propriedade saldo
# a forma de chamar os dois é diferente

print(c1.limite)
c1.limite = 30000   # acessando o setter e setando um novo limite
print(c1.limite)    # acessando a propriedade limite
print(c1.valor_total)
"""


# Importância das properties
# O seguinte código tem os atributos todos públicos


class ContaBancaria:

    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo


contaBancario = ContaBancaria(2479, 11000)
# para acessar os atributos basta fazer objeto.atributo
print(contaBancario.saldo)
print(contaBancario.numero)
# para modificar um atributo basta fazer objeto.atributo = value
contaBancario.saldo = 15000
contaBancario.numero = 2550
print(contaBancario.saldo)
print(contaBancario.numero)

# se os atributos forem mudados de público para privado
# o método de acesso e mudança, objeto.atributo, não é mais válido
# será necessário criar métodos exclusivos de acesso e modificação


class ContaBancaria:

    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo


contaBancario = ContaBancaria(2479, 11000)
# print(contaBancario.saldo) essa forma de acesso gera erro
print(contaBancario.get_saldo())
# se um software tiver sido escrito inicialmente com atributos público
# e o acesso e modificação tiverem sidos feitos por objeto.atributo e os atributos
# mudam para privado, esses métodos de acesso e modificação não serão mais compatíveis
# e todo o código deve ser mudado para getters e setters
# o uso de properties permite que essa mudança seja feita sem que seja necessário mudar
# os métodos de acesso e modificação


class ContaBancaria:

    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @saldo.setter
    def saldo(self, value):
        self.__saldo = value

    @numero.setter
    def numero(self, value):
        self.__numero = value


print("Conta com property")
contaBancario = ContaBancaria(2030, 1100)
print(contaBancario.saldo)
print(contaBancario.numero)
contaBancario.saldo = 100
contaBancario.numero = 5500
print(contaBancario.saldo)
print(contaBancario.numero)
# notar que mesmo com os atributos privados os modos de acesso e modificação
# não precisaram ser alterados
