"""
Len Abs Sum Round
len() -> retorna o tamanho (número de itens) de um iterável

# len() debaixo dos panos
# python executa assim, Dunder (como são chamados o underline)
print('Flamengo'.__len__())

abs() -> retorna o valor absoluto inteiro ou real, ou seja, sem o sinal

print(abs(-10))
print(abs(-23.3))
# Não é possível utilizar o abs pra strings

sum() -> Recebe um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos
lista = [1, 2, 4, 5, 6, 7, 8]
print(sum(lista, 4))
# soma o valor da lista(iterável) mais 4
print(sum(lista, -5))
# subtrai 5 da soma da lista

di = {'a': 1, 'b': 2, 'c': 3}
print(sum(di.values()))
# dicionário/objeto, posso passar o que eu quero do obejto, no caso, os valores

round() -> retorna um número arredondado para n dígito de precisão pós a casa decimal.
Se a precisão não for informada retorna o inteiro mais próximo da entrada

"""

print(round(10.5)) # abaixo/igual de .5 arredonda pra baixo
print(round(10.6)) # acima de .6 arredonda pra cima
print(round(10.66869686, 3)) # 3 casas de precisão

