
arquivo = open('arquivo_teste.txt', 'w')
arquivo2 = open('arquivo_referencia.txt', 'r')

linha = arquivo2.readline()
while linha:    # enquanto houver linha no arquivo, o loop acontecerá
    linha = arquivo2.readline()
    arquivo.write(linha)

arquivo.close()
arquivo2.close()

arquivo = open('arquivo_teste.txt')
lista = arquivo.readlines()
print(f'quantidade de linhas: {len(lista)}')
arquivo.close()