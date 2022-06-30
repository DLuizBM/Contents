"""
Literal type -> obriga que a entrada ou saída de determiando procedimento tenha valores previamente definidos
Union -> com o union é possível fazer o retorno de uma função ser de um tipo, ou de outro. Pode ser aplicado
também no recebimento de valores.
Final -> O final é usado para indicar constantes, assim como no JAVA
Typed dictionaries
Protocols -> Os protocols são usados para definir regras que outros objetos devem seguir

OBS: O python é um linguagem dinâmica, logo, as mudanças feitas pelo typing hinting e dados mais precisos, não causam efeito 
prático, elas são usadas para deixar o código mais legível e indicar a intenção do programador ao criar o código.

def calcula_v1(operacao: str, num1: int, num2: int):
    if operacao == "+": 
        print(f"{num1 + num2}")
    elif operacao == "-": 
        print(f"{num1 - num2}")
    else: 
        raise ValueError(f"Operação inválida {operacao!r}")
        # !r, destaca o valor em aspas simples
calcula_v1("*", 4, 5)


# Literal
# Para fazer o teste correto, é importante usar o mypy
from typing import Literal
def calcula_v1(operacao: Literal["+", "-"], num1: int, num2: int):
    if operacao == "+": 
        print(f"{num1 + num2}")
    elif operacao == "-": 
        print(f"{num1 - num2}")
    else: 
        raise ValueError(f"Operação inválida {operacao!r}")

calcula_v1("*", 5, 6)


# Union
from typing import Union
def soma(num1: int, num2: int, num3: Union[int, str]) -> Union[int, str]:
    resultado = num1 + num2
    if resultado > 50:
        return f"Resultado muito grande: {resultado}"
    else:
        return resultado


# Final
from typing import Final

PI: Final = 3.1415

print(PI)

PI = 2.71

print(PI)
# Como foi definida como Final, não pode ser atribuído um novo valor para PI, lembrando que o Python permite,
# mas que a intenção do programador é que isso não ocorra, por isso o Final foi utilizado

from typing import final

@final 
class Pessoa:
    # quando uma classe é decorada com @final, significa que ela não pode ser herdada
    pass

class Estudante(Pessoa): # Pessoa não pode ser herdade por conta do final
    pass

    @final
    def estudar(self):
        # quando um método é decorado com @final, significa que ele não pode ser sobrescrito
        print("Estudando")

class Estagiario(Estudante):
    pass

    def estudar(self): # estudar não pode ser sobrescrito por conta do final
        print("Estudando e estagiando")

# Typed dictionary
from typing import TypedDict

# É possível criar objetos usando classes, com em javascript
class Curso(TypedDict):
    versao: str
    atualizacao: int


python = Curso(versao='3.8.5', atualizacao=2020)
print(python)

"""

# Protocols

from typing import Protocol

class Curso(Protocol):
    titulo: str
    # Classes que herdam Protocol não podem ser instanciadas
    # A classe Curso define que é obrigatório que um curso tenha um título para ser usado, se um método espera receber
    # uma classe Curso e usa o título em algum procedimento

def estudar(valor: Curso) -> None:
    print(f"Estudando o curso {valor.titulo}")
    # O parâmetro estudar é do tipo Curso e o procedimento print usa título
    # Sendo assim, é necessário que o argumento que for passado para esse método, seja uma classe que possui o 
    # atributo título, se não, haverá erro.

class Python:
    titulo: str = "Python"
    # A classe Python é um curso que possui o atributo título, sendo assim, é possível que ela seja passada para
    # o método estudar.

curso = Python()
estudar(curso)

num: float = 0.5896478963214
print(f"{num:.2f}")
print(f"{num=}")
# fstrings, print a variável com seu respectivo valor