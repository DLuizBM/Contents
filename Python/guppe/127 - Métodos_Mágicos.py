"""
POO - Métodos mágicos
Métodos mágicos são todos os métodos que utilizam dunder
Ex: dunder init -> __init__()

print(dir(object))
# todos os métodos mágicos(builtins) vem da classe object


# método repr


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return self.titulo


livro1 = Livro('Python Rocks', 'Geek University', 1000)

print(livro1)
# sem o método repr, a saída seria um endereço de memória
# com o método repr a saída vai ser a informação corresponde do objeto(no caso, o título, mas é possível mudar no return



# Dunder str
# Enquanto repr é usado para desenvolvedores, str é para mostrar para o usuário
# o str tem prioridade sobre o repr, logo se esses 2 métodos estiverem no código
# somente o str será executado


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return f'{self.titulo} {self.paginas}'

    def __len__(self):  # retorna o tamanho do objeto
        return self.paginas     # definindo como tamanho do objeto o número de páginas

    def __del__(self):  # modificando o método del
        print('Um objeto do tipo livro foi deletado')


livro1 = Livro('Python Rocks', 'Geek University', 1000)

print(repr(livro1))
# se quisermos que seja dada a representação, devemos passar dessa forma
print(livro1)
print(len(livro1))
# só é possível usar len no objeto, se o método len foi colocado dentro da classe
del livro1
# saída: Um objeto do tipo livro foi deletado

# Método add


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    # def __del__(self):se o método del estiver no código,o python não vai guardar os elementos na memória e vai deletar
        # gerando duas mensagens de 'Um objeto do tipo livro foi deletado', uma para cada livro (cada objeto)
        # print('Um objeto do tipo livro foi deletado')

    def __add__(self, other):   # representação po método da adição/concatenação(para strings)
        return f'{self} - {other}'
        # como há o método __str__ para representar os livros pelo título
        # não é necessário colocar self.titulo e other.titulo, pois o método
        # add já sabe que deve somar/concatenar os titulos


livro1 = Livro('Python Rocks', 'Geek University', 1000)
livro2 = Livro('Harry Pother', 'J.K Rowling', 1000)


print(livro1 + livro2)
# sem o método add, essa operação vai gerar um erro
# com o método add, self vai ser o primeiro livro(livro1) e outro o segundo(livro2)

"""
# Método __mul__


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __mul__(self, other):
        if isinstance(other, int):  # se a instância other é do tipo inteiro
            msg = ''
            for _ in range(other):
                msg += ' ' + str(self)  # self -> recebe o que foi definido no str, assim sendo, o título
            return msg
        return f'Não foi possível concatenar'


livro1 = Livro('Python Rocks', 'Geek University', 1000)
print(livro1 * 3)
# saída:  Python Rocks Python Rocks Python Rocks

print(dir(object))
# todos os métodos mágicos(builtins) vem da classe object