"""
Escrevendo um iterador customizado
-Para entender é precisa saber Orientação à Objetos
"""
# Criando um range() com o nome de contador()
class contador:
    def __init__(self, menor, maior): # quando se trabalha com classes, uma função passa a ser de chamada de método
        self.menor = menor
        self.maior = maior
    # a função __init__ é uma função especial chamada de construtor
    # o construtor é a função responsável por criar os objetos a partir da classe
    # sempre que houver uma função dentro de uma classe, vai haver um self, ele representa o próprio objeto
    def __iter__(self):
        return self
    # retornando ele próprio(o próprio objeto)
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration
        # quando o número não for mais menor, executará o StopIteration parando

for n in contador(1, 100):
    print(n)

