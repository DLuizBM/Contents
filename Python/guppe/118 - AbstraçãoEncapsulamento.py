"""
Abstração e encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico
utilizando classes

Imagine que temos uma classe chamada pessoa e o atributo privado chamado __nome e um método privado chamado falar __
Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas python não bloqueira
esse acesso fora da classe. Com python acontece o fenômeno chamado Name Mangling, que faz uma alteração
na forma de se acessar os elementos privados, conforme:

_Classe__elemento

Exemplo:
instância._Pessoa__nome
instância._Pessoa__falar()

Abstração: em POO, é o ato de expor apenas os dados relevantes de uma classe, escondendo atributos e métodos
privados de usuários.


# Exemplo de código com atributos públicos


class Conta:
    contador = 400

    def __init__(self, saldo, limite, titular):
        self.numero = Conta.contador
        self.saldo = saldo
        self.limite = limite
        self.titular = titular
        Conta.contador += 1

    def extrato(self):
        return f'O titular {self.titular} da conta {self.numero}, pussui saldo de {self.saldo} e limite de {self.limite}.'


conta1 = Conta(2000, 5000, 'Hamilton')
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)
print(conta1.extrato())

conta1.limite = 10000
conta1.saldo = 5000
print(conta1.__dict__)
# Com os atributos públicos o sistema fica inseguro e é possível fazer modificações dos atributos fora da classe
# O ideal é que os atributos que os usuários não devem ter acesso, sejam privados




# Exemplo com atributos privados
# Tudo dentro de uma classe está encapsulado, a única diferença é o nível de visibilidade

class Conta:
    contador = 400

    def __init__(self, saldo, limite, titular):
        self.__numero = Conta.contador
        self.__saldo = saldo
        self.__limite = limite
        self.__titular = titular
        Conta.contador += 1

    def extrato(self):
        return f'O titular {self.__titular} da conta {self.__numero}, pussui saldo de {self.__saldo} e limite de {self.__limite}.'

    def depositar(self, valor):
        self.__saldo += valor


conta1 = Conta(2000, 5000, 'Hamilton')

# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.limite)
# conta1.limite = 10000
# conta1.saldo = 5000
# Esses comandos não vão mais funcionar, pois agora com os atributos privados, não se tem mais acesso à eles

# Lembrando que é possível acessar e fazer alteração com o name mangling, porém isso não é certo
print(conta1._Conta__titular) # Hamilton
conta1._Conta__titular = 'Alonso'
print(conta1._Conta__titular) # Alonso
print(conta1.extrato())

print(conta1.__dict__)
conta1.depositar(500)
print(conta1.__dict__)

"""

# Exemplo - método de transferência de valores entre contas


class Conta:
    contador = 400

    def __init__(self, saldo, limite, titular):
        self.__numero = Conta.contador
        self.__saldo = saldo
        self.__limite = limite
        self.__titular = titular
        Conta.contador += 1

    def extrato(self):
        return f'O titular {self.__titular} da conta {self.__numero}, pussui saldo de {self.__saldo} e limite de {self.__limite}.'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, contadestino, valor):
        # 1 - sacar o dinheiro da conta de origem
        if valor <= self.__saldo:
            self.sacar(valor)
            # 2 - transferir o valor para a conta destino
            contadestino.__saldo = contadestino.__saldo + valor
        else:
            print(f'Saldo indisponível.')


conta1 = Conta(2000, 5000, 'Hamilton')
conta2 = Conta(1000, 3500, 'Alonso')
print(conta1.__dict__)
print(conta2.__dict__)
conta1.transferir(conta2, 200)
print(conta1.__dict__)
print(conta2.__dict__)

