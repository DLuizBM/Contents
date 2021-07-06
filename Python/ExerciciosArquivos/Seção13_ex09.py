a1 = input('Arquivo 1:')
a2 = input('Arquivo 2:')

try:
    arquivo1 = open(a1, 'r')
    arquivo2 = open(a2, 'r')
except FileNotFoundError as err:
    print(f'Ops! Um erro ocorreu ao abrir o arquivo: {err}')
else:
    arquivo3 = open('arquivo_teste2.txt', 'a')
    linha = arquivo1.readline()
    while linha:
        arquivo3.write(linha)
        linha = arquivo1.readline()

    linha = arquivo2.readline()
    while linha:
        arquivo3.write(linha)
        linha = arquivo2.readline()

    arquivo1.close()
    arquivo2.close()
    arquivo3.close()

finally:
    print('Executado!!')