class pessoa:
    
    def __init__(self, nome):
        self.__nome = nome;
        
    @property
    def nome(self):
        return self.__nome


p1 = pessoa("Messi")
p2 = pessoa("Neymar")

lst = [{p1: 1}, {p2: 2}]

key = lst[0].items()
# items retorna um dict_items que é um view object. O view object contém os pares chave valor de um dicitonário
# na forma de uma tuplas dentro de uma lista. 
# Ex: {'a': 1, 'b': 2}
# dict_items[('a', 1), ('b', 2)]
# list({'a': 1, 'b': 2}.items())
# [('a', 1), ('b', '2')]
print(list(key)[0][0].nome)