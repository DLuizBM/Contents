class Person:
    def __init__(self, name, age, heigth):
        self.__name = name
        self.__age = age
        self.__heigth = heigth

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def heigth(self):
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        self.__heigth = value

