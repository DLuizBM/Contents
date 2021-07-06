"""
Sistemas de arquivos e navegação

Para fazer o uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer o uso do módulo OS

OS -> Operating System


# Import do os

import os

# Pegar o diretório atual
print(os.getcwd())
# Saída: /home/divinoluiz/PycharmProjects/guppe
# Retorna o caminha absoluto

# Para mudar o diretório, basta usar a função chdir()
os.chdir('..') # dois pontos significam que deve voltar um diretório, assim como usado no terminal
print(os.getcwd())
# Saída: /home/divinoluiz/PycharmProjects


# Podemos checar um diretório, pra saber se é relativo ou absoluto

print(os.path.isabs('/home/divinoluiz/PycharmProjects/guppe'))
# Saída: True -> true significa que é absoluto

print(os.path.isabs('/home/divinoluiz/PycharmProjects'))
# Saída: True


import os
# Podemos identificar o sistema operacional com o módulo os

print(os.name)
# Saída: posix

# Oferece mais informações sobre o os
print(os.uname())


import sys
print(sys.platform)
# Saída: linux


import os

print(os.getcwd()) # /home/divinoluiz/PycharmProjects/guppe

os.chdir('..')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())

res = os.path.join(os.getcwd(), 'PycharmProjects')
# juntando o diretório /home/divinoluiz/PycharmProjects/guppe com PycharmProjects
# pode-se colocar mais parâmetros, para ser juntado, exemplo: se houvesse um outro diretório
# dentro de PycharmProjects, poderíamos colocar uma terceira, quarta string, para serem juntadas
# e assim ir para o diretório especificado

os.chdir(res)
# O os.chdir vai levar para o diretório especificado
print(os.getcwd())

# Podemos listar todos os arquivos e diretórios

import os
print(os.listdir()) # devolve uma lista com todos os arq e dir dentro do diretório analisado
print(len(os.listdir()))


# lista o que está dentro do atual diretório
os.chdir('..')
print(os.listdir())
print(len(os.listdir()))
print(len(os.listdir('Exercícios_coleções')))
# especificando quantos arquivos há dentro de 'Exercícios_coleções'


"""

# Listando com mais detalhes

import os
scanner = os.scandir()
arquivos = list(scanner)
print(arquivos)

print(arquivos[0])
print(arquivos[0].inode) # -> vai devolver apenas o endereço de memória
# arquivos[0].inode() -> com os parênteses é porque estou executando,
# sem parênteses devolve somente o endereço de memória
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].is_symlink())
print(arquivos[0].name)
print(arquivos[0].path)

# Quando usamos a função scandir(), após seu uso, devemos fechá-la
scanner.close()






