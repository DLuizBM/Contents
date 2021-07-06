"""
Seek e Cursors

seek() -> usada para movimentar o cursor pelo arquivo. Ela recebe uma parâmetro que
indica onde queremos colocar o cursor


arquivo = open('texto.txt')
print(arquivo.read())
print(' ')
# Movimentando o cursor pelo arquivo com a função seek
arquivo.seek(0) # a posição 0 indica o início do arquivo(primeiro caractere), fazendo isso o cursor volta
                # para o início e pode-se imprimir o arquivo de novo

print(arquivo.read())
print(' ')
arquivo.seek(21) # começa a ler a partir do caractere 21
print(arquivo.read())

# Lendo linha por linha com a função readline()

arquivo = open('texto.txt')
print(arquivo.readline())
# lê linha por linha, se for executado só uma vez, imprime apenas a primeira linha
# retorna uma string
print(arquivo.readline()) # lendo a segunda linha
ret = arquivo.readline() # pegando a 3 linha
print(ret.split(' '))   # transformando a 3 linha em um lista de strings


# readlines() -> lê todas as linhas e coloca cada linha como sendo um elemento de uma lista
# ou seja, faz uma lista de strings, com cada string sendo uma linha

arquivo = open('texto.txt')
print(arquivo.readlines())
arquivo.seek(0)
ret = arquivo.readlines() # pega somente as linhas que tem conteúdo
print(len(ret))
# descobrindo a quantidade de linhas no texto


# OBS: quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
# no disco do computador e o programa, essa conexão é chamada de streaming. Ao finalizar
# os trabalhos com o arquivo, devemos fechar essa conexão. Para isso utilizamos a função close()

arquivo = open('texto.txt')

print(arquivo.read())


print(arquivo.closed)
# Indica se o arquivo está fechado ou aberto. True se tiver fechado, false se aberto

arquivo.close()

print(arquivo.closed)
# OBS: se tentarmos manipular o arquivo depois de fechado, será apresentado um ValueError

arquivo = open('texto.txt')
print(arquivo.read(51))
# lendo apenas os 50 primeiros caracteres
##################################################################################

O bloco With

- O bloco with serve para criar um contexto de trabalho onde os recursos utilizados
são fechados após o bloco. Forma pythonica de se trabalhar com arquivos

"""
with open('texto.txt') as arquivo: # as apelido
    print(arquivo.readline())
    print(arquivo.closed) # False: pois dentro do bloco with, o arquivo ainda está abert

print(arquivo.closed) # True, pois fora do bloco with, o arquivo já está fechado
# print(arquivo.read())
# Saída: ValueError: I/O operation on closed file.
# Com o bloco with o arquivo é aberto e fechado após sair do bloco, fora no bloco ele não é mais
# manipulável


