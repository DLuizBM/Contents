class Book:
    def __init__(self):
        self._title = "Book"

    """
    ao reescrever métodos built-in é possível dar para a classe uma string, quando chamado método str(class),
    um tamanho quando chamado o método len(class), etc, algo que não é possível se esses métodos não forem reescritos.
    """

    def __str__(self):
        return "these are real books"

    def __len__(self):
        return 42

book = Book()
print(book)
# o método __str__ é usado para retornar uma representação de string de um objeto, se for printado um objeto, ele mostrará
# a string correspondente definida no método __str__, se ele estiver definido. Funciona como o toString de JAVA.
print(len(book)) 
# a função len() chama o método __len__() do objeto, ou seja, se esse método estiver definido, qualquer objeto pode ter um len

age = 26
print(len(age))
# gera erro, pois o objeto do tipo int não possui método __len__