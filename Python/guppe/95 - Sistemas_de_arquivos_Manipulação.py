"""
Sistemas de arquivos - Manipulação


import os
# Descobrindo se um arquivo existe

# Paths(Caminhos) relativos.
print(os.path.exists('texto.txt'))
# Existe o arquivo 'texto.txt', saída: True

# Diretório
print(os.path.exists('MyPackage')) # True
print(os.path.exists('MyPackage/package2')) # True
# Dentro do diretório MyPackage existe package2? true
print(os.path.exists('MyPackage/package2/módulo_3.py'))
# Dentro do diretório MyPackage no package2 existe o arquivo módulo_3.py? true

# Paths(absolutos)
print(os.path.exists('/home/imagens')) # false
print(os.path.exists('/home/divinoluiz')) # true


import os

# Criando arquivos

# Forma 1
open('arquivo_teste.txt', 'w').close()

# Forma 2
# open('arquivo_teste.txt', 'a').close()

# Forma 3
#with open('arquivo_teste.txt', 'w') as arquivo:
    #pass
    # pass significa que nada deve ser feito

import os
# Melhor forma de se fazer

#os.mknod('arquivo_teste.txt')
os.mknod('MyPackage/arquivo_teste.txt')
# Criando dentro de um diretório especificado


# Criando diretórios

import os
# Path relativo
os.mkdir('MyPackage/templates')

# Path absoluto
os.mkdir('MyPackage/templates')
# por padrão é criado no diretório que está sendo executado
# no exemplo acima foi especificado o caminho
# se não tivermos permissão para criar o diretótio, será informado um perssion error


# Criando multi diretórios
import os
os.makedirs('MyPackage/template/css/js')
# Dentro de MyPackage crie o diretório template, dentro de template css e de css js


import os
os.makedirs('MyPackage/template/css/js', exist_ok=True)
# Se o diretório já existir ignora, não apresenta erro


# Renomeando arquivos e diretórios
import os
#os.makedirs('MyPackage/template/css/js')
os.rename('MyPackage/template/css', 'MyPackage/template/CSS')
# Para alterar o nome, deve-se informar o caminho completa tanto do nome original, quanto para o novo nome
# se isso não for feito o arquivo/diretório é retirado de dentro de onde está


import os
os.rename('MyPackage/arquivos.txt', 'MyPackage/arquivo_TESTE.txt')

# Removendo arquivos
import os


# OBS: ATENÇÃO!!! Deve-se tomar cuidado com os comandos de deleção, pois ao deletar um arquivo/diretório
# eles não vão para a lixeira, eles somem

os.remove('arquivo_teste.txt')
# os.remove -> remove apenas arquivos
# Caso o arquivo não exista teremos o FileNotFoundError

# OBS: caso for informado um diretório ao invés de um arquivo, será um IsADirectoryError


# Removendo diretórios vazios
import os
os.rmdir('MyPackage/template')
# os.rmdir só serve para diretórios vazios
# Se o diretório contiver algum arquivos, será apresentado um erro Directory not empty
# Se o diretório não existir será dado um file not found error

# Removendo um árvore de arquivos

import os

for arquivo in os.scandir('MyPackage/template'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# removendo uma árvore de diretórios vazios

import os
os.removedirs('MyPackage/template/CSS/js')
# ir até o último diretório que se quer excluir
# se o diretório não estiver vazio, apresentará erro
# lembrando que arquivos deletados com python não vão para a lixeira, são apagados
# é possível instalar um pacote que faz o envio para a lixeira, que é o send2trash
# para instalar basta rodar sudo apt-get install lsb-core e pip install send2trash


# Trabalhando com diretórios temporários

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'criei o arquivo temporário em {tmp}.')
    with open(os.path.join(tmp, 'arquivotemporario.txt'), 'w') as arquivo:
        arquivo.write("Arquivo criado \n")
    input()
# criando um diretório temporário e dentro dele um arquivo colocando o arquivo
# o input é para segurar o sistema, pois como os arquivos são temporários, ao finalizar o programa
# os arquivos somem


# Trabalhando com arquivos temporários
import os
import tempfile

# criando arquivo temporário
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Arquivo temporario\n')
    # b significa que está passando para binário
    # em arquivos temporários são conseguimos escrever bits, por isso estamos passando a string para bitsp
    tmp.seek(0)
    print(tmp.read())
    input()

"""
import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Arquivo temporario \n')
print(arquivo.name)
print(arquivo.read())
# importante colocar arquivo.read() para que o conteúdo do arquivo seja mostrado na pasta temporário onde ele foi criado
input()
arquivo.close()

