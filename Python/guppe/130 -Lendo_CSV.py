"""
Lendo arquivos CSV
CSV -  Comma Separated Values - Valores separados por vírgula
# Podem haver vários tipos de separador
# Separador pode ser vígula
1, 2, 3, 4, 5

# Separador por ponto e vírgula
1; 2; 3; 4; 5

# Forma possível, mas não recomendada de se fazer a limpeza dos dados (com arquivos csv)

with open('original.csv') as arquivo:
    dados = arquivo.read()
    print(dados)
    dados = dados.split(',')[2::]
    # separando por vírgulo e começando do elemento 2
    print(dados)

- O python possui duas formas diferentes para ler dados de um arquivo CSV
    -reader -> Permite que iteremos sobre as linhas do arquivo csv como listas
    -dictReader -> Permite que iteremos sobre as linhas do arquivo csv como OrderedDict
    -OBS: por padrão os métodos reader e dictreader utilizam a vírgula como separador

lista = [1, 2, 3, 4]
lista = iter(lista)
next(lista)
print(list(lista))


# Reader

from csv import reader

with open('original.csv') as arquivo:
    csv = reader(arquivo)
    # reader devolve um iterator, assim sendo é possível fazer
    next(csv)
    # dessa forma dando um next, o csv no for começa a partir da segundo linha
    # devolve listas
    for linha in csv:
        print(linha)
        # cada linha é uma lista


# Dict Reader

from csv import DictReader

with open('original.csv') as arquivo:
    csv = DictReader(arquivo)
    for linha in csv:
        print(linha)
# cada linha é um dicionário onde as chaves são os itens do dicionário e os valores
# correspondem as informações
# ex: {'Nome': 'Ryu', 'País': 'Japão', 'Altura (em cm)': '175'}
# Nome, país e altura são as chaves

"""

from csv import DictReader

with open('original.csv') as arquivo:
    csv = DictReader(arquivo, delimiter=',')
    # delimiter é onde se especifica o separador, serve tanto para DictReader como para reader
    for linha in csv:
        print(linha)