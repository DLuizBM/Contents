"""
Recebendo dados do usuário

Todo dado recebido via input() é string

Em pyhton, string é tudo que estiver em:

Aspas simples: 'Angelina'
Aspas duplas: "Angelinas"
Aspas simples triplas: '''Angelina''' """
# Aspas duplas triplas: """Angelina"""


# Entrada de dados

# print("Qual o seu nome?")
nome = input("Qual o seu nome?")

# print("Qual a sua idade?")
# idade = input("Qual a sua idade?")
idade = int(input("Qual a sua idade?"))

# Processamento de dados

# Saída de dados

# Exemplo de print do python 2.x
# print("Seja bem vindo(a) %s !" % nome)
# print("%s tem %s anos" % (nome, idade))

# Exemplo de print do python 3.x
# print('Seja bem vindo(a) {0}'. format(nome))
# print('{0} tem {1} anos'. format(nome, idade))

# Exemplo de print do python 3.7

print(f"Seja bem vindo(a){nome}")
print(f"{nome} tem {idade} anos.")

"""
int(variavel), está fazendo o cast, ou seja,
a conversão de string em int

"""
# print(f"{nome} nasceu em {2019 - int(idade)}.")
print(f"{nome} nasceu em {2019 - idade}.")


"""
Em pyhton é possível fazer a reatribuição,
que é quando se declara um valor para uma variável e depois dá-se a ela
um novo valor
ex:

num =  42
print(num)
print(type(num))

num = 'Geek'
print(num)
print(type(num))
"""




