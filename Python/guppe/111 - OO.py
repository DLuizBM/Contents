"""
Orientação à objetos
- Classe: Modelo do objeto
- Atributo: Característica do objeto
- Métdos -> são funções dentro de classes (comportamento do objeto)
- Métodos construtor -> método para criar objetos a partir da classe
- Objetos/instâncias: Elementos criados a partir da classe

"""


class Produto:
    pass

# pass é somente para dar a identação, sem o pass terá erro

ps4 = Produto() # Produto() -> construtor padrão da classe, reparar que é um método, pois estou abrindo e fechando ()
# criei o ps4 a partir do construtor da classe Produto(), ou seja, estou instanciando um objeto
# criando um objeto
# ps4 será um objeto da classe Produto
print(type(ps4))
# saída: <class '__main__.Produto'>

