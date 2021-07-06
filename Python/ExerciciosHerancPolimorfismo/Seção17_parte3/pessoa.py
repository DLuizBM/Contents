class Person:
    def __init__(self, code, name, age):
        self.__code = code
        self.__name = name
        self.__age = age
        self.__choice = 0

        print('This is the standart constructor.')

    # criando o método get, para que outra classe que herde a classe Person consiga
    # acessar o nome, sem precisar usar name mangling
    @property
    def getName(self):
        return self.__name

    def display(self, choice=0):
        self.__choice = choice
        if self.__choice == 1:
            self.__choice = 0
            return f'Code: {self.__code}\nName: {self.__name}\nAge: {self.__age}'
        else:
            return f'Code: {self.__code}\nName: {self.__name}\n'
