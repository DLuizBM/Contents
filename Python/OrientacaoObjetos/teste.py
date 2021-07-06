"""
class Pessoa:
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    def dados(self):
        print(f'Nome: {self.__nome}\nTelefone: {self.__telefone}.')


dic = {'hamilton': Pessoa('hamilton', 5555), 'alonso': Pessoa('alonso', 66666)}
# dic.pop('alonso')
# print(dic)
# pop remove o item especificado do dicionário
p = list(map(lambda x: dic[x].dados(), dic.keys()))
# print(p)
# igualado p, [none] aparece no final

lista = [1, 2, 3, 4]
def printa(x):
    print(x + 10)
(list(map(lambda x: printa(x), lista)))
# forma correta para usar no dicionário e não aparecer o [none]
# parêntese é opcional

p1 = list(map(lambda x: x + 100, lista))
print(p1)

"""

lista = [1, 2, 3, 4]
p = list(filter(lambda x: x == 1, lista))
print(bool(p))
