"""
ANY E ALL

all() -> retorna true, se todos os elementos do iterável são verdadeiros ou se o
iterável está vazio
- Utilizado para fazer checagem

# Exemplos all

print(all([0, 1, 2, 3, 4]))     # Todos os número são True?
# Como 0 é false, o retorno é false
print(all([1, 2, 3, 4]))
# Retorno é true
print(all([]))
# Retorno é true
print(all(['Senna']))
# Retorno é true

nomes = ['Messi', 'Mozer', 'Maradona']
print(all([nome[0] == 'M' for nome in nomes]))
# se todos os nome[0] é igual a 'M', não é necessário o if

# Exemplo para testar a condição acima, de adicionar na lista
nome = ['divino', 'luiz']
res = []
if nome[0][0] == 'o':
    res.append(bool(nome[0][0]))
else:
    res.append(not bool(nome[0][0]))
print(res)




print(all([letra for letra in 'jk' if letra in 'aei']))

# Nesse caso, o retorno será true, pois como nenhuma letra comparado entra a condição
# a lista estará vazia, e lista vazia (iterável vazio) retorna true
# o que está sendo feito no list comprehension
# for letra in 'ae':
#    if letra in 'aeiou':
#        print(letra)

print(all([letra if letra in 'aei' else not letra for letra in 'jk']))
# para imprimir o valor, booleano false corretamente, deve ser feito mais uma condição
# e usar o operado lógico not
# O que está sendo feito no list comprehension

for letra in 'jk':
    if letra in 'aeiou':
        print(all(letra))
    else:
        # letra = 0
        # print(all([letra]))
        print(all([not letra]))
        # lembrando que o not, nega a variável, logo se ela possui um valor (booleaneo true)
        # então aplicando o not ela terá valor (booleano) false, se aplicado de novo
        # o valor booleano retorna para true

###################################################################################

any() -> Retorna true se qualquer elemento do iterável for verdadeiro, se to iterável
estiver vazio, retorna false

all - se todos forem verdadeiros retorna true
any - se algum for verdadeiro retorna true

"""
print(all([0, 1, 2, 3])) # False
print(any([0, 1, 2, 3])) # True

nomes = ['Messi', 'Mozer', 'Maradona', 'Zico']
print(all([nome[0] == 'M' for nome in nomes])) # False
# A lista criada = [true, true, true, false] -> por isso false (all, tem um false, então false), por causa da condição do all
print(any([nome[0] == 'M' for nome in nomes])) # True
# A lista criada = [true, true, true, false] -> any, tem um true, então é true

print(all([num for num in [1, 2, 3, 4] if num % 2 == 0]))
# Faça uma lista com todos os números pares, como a lista terá [2, 4] e ambos são true, a saída será true
# Saída -> true

print(all([num if num % 2 == 0 else not num for num in [1, 2, 3, 4]]))
# Jeito correto de usar all, para saber se todos os elementos de um iterável se encaixam
# Na condição especificada, pois pode haver condições que preenchem a lista com um valor verdadeiro
# mas nem todos os iteráveis são true
# Saída -> False

print(any([num for num in [1, 2, 3, 4] if num % 2 == 0]))
# Saída -> true

lista = [1, 2, 4]
print(any([num for num in lista if num % 3 == 0]))

