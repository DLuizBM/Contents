"""
Geradores: Conhecidos como generators, são iterators
OBS: O contrário não é verdadeiro, nem todo iterator é um generator

- Generator podem ser criadas com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criadas com Expressões geradoras;

Diferenças entre funções e generator function (funções geradoras)

-------------------------------------------------------------------------------
| Funções                                 |generator function
-------------------------------------------------------------------------------
| utilizam return                        |utilizam yield
-------------------------------------------------------------------------------
| retorna uma vez                       |podem utilizar yield múltiplas vezes
-------------------------------------------------------------------------------
| quando executada, retorna um valor   |quando executada, retorna um generator

"""
# Exemplo de generator function

def conta(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

        # quando se usa o yield ele não sai da função(diferentemente do return), ele retorna e aguarda
        # até um próximo next() para ir pra próxima linha

gen = conta(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Gerando todos de uma vez
gen = conta(10)
print(list(gen))

lista = [1, 2, 3, 4]
print([num for num in lista if num % 2 == 0])
