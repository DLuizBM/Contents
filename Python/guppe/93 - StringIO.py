"""
String I/O
OBS: Para ler ou escrever dados em arquivos do sistema operacional o software precisa
ter permissão (para ler e escrever)

String I/O -> utilizado para ler e criar arquivos em memória quando não se tem permissão para criar
arquivos em disco. Deve-se fazer o import

"""
from io import StringIO

mensagem = 'Olá mundo!!!'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para
# inserirmos textos depois

arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# Agora podemos usar tudo que sabemos de arquivos
print(arquivo.read())
# com o print(arquivo.read()) antes do seek(), o print depois de seek tem a seguinte saída:
# Olá mundo!!!Estou apenas na memória!
# sem o print antes do seek():
# Estou apenas na memória!
# Isso ocorre pq na chamada (read()), olá mundo!!! fica salvo em memória, e aí no segundo print ele já está
# salvo lá.


arquivo.write('Estou apenas na memória!')

arquivo.seek(0)

print(arquivo.read())
# O que acontece com o stringIO é que não é criado um arquivo normal, ele é criado apenas na memória.
