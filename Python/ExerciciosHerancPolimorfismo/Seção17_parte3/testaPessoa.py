from Seção17_parte3 import pessoa


class Test(pessoa.Person):
    def __init__(self, code, name, age):
        super().__init__(code, name, age)

    def super_display(self, choice=0):
        if choice == 1:
            return self.getName     # acessando o atributo name pelo método, forma correta
            # return self._Person__name  acessando o atributo name pelo namemangling
        elif choice == 2:
            return self._Person__code
        elif choice == 3:
            return self._Person__age


person = Test(44, 'Hamilton', 34)
print(person.super_display(2))
print(person.display(1))