
def concatena_string(car, **kwargs):
    """
    Função que recebe 2 strings e concatena uma quantidade de caracteres (Escolhida pelo usuário
    da segunda string a primeira.
    :param car:
    :param kwargs:

    """
    # Transformando em lista de caractere os valores do dicionário
    str1 = list(kwargs['string1'])
    str2 = list(kwargs['string2'])

    for i in range(0, car):
        str1.append(str2[i])

    str1 = ''.join(str1) # Juntando todos os caracteres da lista pra formar a string
    print(str1)

str1 = input("Digite a string 1: ")
str2 = input("Digite a string 2: ")
c = int(input("Digite o número de caracteres da string 2 que devem"
              "ser concatenados a primeira string: "
              ))

concatena_string(c, string1=str1, string2=str2)
# kwargs transforma tudo em dicionário, lembrando que para passar um argumento para o parâmetro
# ele deve ir no formato chave/valor. No programa é passado 'string1=str1 e string2=str2'
# são passados as chaves string1 e 2 e os valores str1 e 2
