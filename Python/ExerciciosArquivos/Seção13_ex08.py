a1 = input('Arquivo a ser lido:')
a2 = input('Arquivo a ser escrito:')
try:
    with open(a1, 'r') as arquivo2:
     with open(a2, 'w') as arquivo:
        linha = arquivo2.readline()
        while linha:
            LINHA = ''
            for letra in linha:
                if letra == letra.upper():
                    LINHA = LINHA + letra
                else:
                    LINHA = LINHA + letra.upper()
            arquivo.write(LINHA)
            linha = arquivo2.readline()
except FileNotFoundError as erra:
    print(f'Ops! Foi encontrado o seguinte erro: {erra}')


with open('arquivo_teste.txt', 'r') as arquivo:
    print(arquivo.read())
