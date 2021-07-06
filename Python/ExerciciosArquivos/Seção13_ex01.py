# Criando e escrevendo no arquivo
arquivo = open('arquivo_teste.txt', 'w')
carac = input()
while carac != '0':
    arquivo.write(carac)
    carac = input()

arquivo.close()

# Reabrindo o arquivo para se fazer a leitura
arquivo = open('arquivo_teste.txt')
print(arquivo.read())

arquivo.close()
