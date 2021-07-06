"""
Poo - Herança (Inheritance)

-A ideia de herança é a de reaproveitar código e extender as classes. Se uma classe for genérica
o suficiente, é possível reaproveitar essa classe. Herdando atributos e métodos dessa classe.

- A classe herdada é conhecida por:
    -super classe;
    -classe mãe;
    -classe pai;
    -classe base
    -classe genérica
- Quando uma classe herda de outra classe, ela é chamada de:
    -sub classe;
    -classe filha;
    -classe específica;


# Exemplo -> fazer um sistema com funcionário e cliente, sabendo que cliente e funcionário tem atributos em comum


class Pessoa:   # super classe
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    # é possível que as classes Cliente e Funcionário também acessem esse método


class Cliente(Pessoa):  # Classe filha
    "" Cliente herda de pessoa, cliente é do tipo pessoa""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # Forma comum
        # super() é modo de fazer acesso ao construtor da super classe

        # Pessoa.__init__(self, nome,sobrenome, cpf)outra forma de fazer acesso ao construtor da Super Classe, ñ é comum
        self.__renda = renda


class Funcionario(Pessoa):  # Classe filha
    "" Funcionário herda de pessoa, funcionário é do tipo pesso""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


c1 = Cliente('Hamilton', 'Lewis', 5555, 1234)
print(c1.__dict__)
# Saída: {'_Pessoa__nome': 'Hamilton', '_Pessoa__sobrenome': 'Lewis', '_Pessoa__cpf': 5555, '_Cliente__renda': 1234}
# é possível ver qual atributo vem de qual classe



Sobre escrita de métodos (Overrinding)

- Ocorre quando reescrevemos um método da super classe em classes filhas
"""

# reescreveno o método nome_completo adicionando a matrícula para funcionário


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def get_cpf(self):
        return self.__cpf


class Cliente(Pessoa):  # Classe filha
    """ Cliente herda de pessoa, cliente é do tipo pessoa """
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # Forma comum
        self.__renda = renda


class Funcionario(Pessoa):
    """" Funcionário herda de pessoa, funcionário é do tipo pesso """
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # com super é posível fazer acesso a tudo da classe pai
        self.__matricula = matricula

    def nome_completo(self):    # Método reescrito
        print(super().nome_completo())
        # modo de executar o método nome_completo da forma que foi inicialmente escrito na super classe
        # acessando o cpf com name mangling
        # print(self._Pessoa__cpf)
        print(self.get_cpf())
        return f'Matricula: {self.__matricula} Nome: {self._Pessoa__nome}'


f1 = Funcionario('Hamilton', 'Lewis', 5555, 1234)
c1 = Cliente('Fernando', 'Alonso', 7777, 2345)
print(f1.nome_completo())
# Saída: Matricula: 1234 Nome: Hamilton
# todas as vezes que o método nome completo for chamado dentro da classe Funcionário, não será mais
# apresentado o nome completo e sim a matrícula e o nome
# diferentemente do que acontece com a classe Cliente que toda vez que chamar o método nome_completo()
# mostrará o nome completo
print(c1.nome_completo())
# Saída: Fernando Alonso

