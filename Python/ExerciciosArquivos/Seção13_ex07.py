with open('arquivo_referencia.txt', 'r') as arquivo2:
    with open('arquivo_teste.txt', 'w') as arquivo:
        linha = arquivo2.readline()
        while linha:
            Linha = ''
            for vogal in linha:
                if vogal.lower() == 'a':
                    Linha = Linha + '*'
                elif vogal.lower() == 'e':
                    Linha = Linha + '*'
                elif vogal.lower() == 'i':
                    Linha = Linha + '*'
                elif vogal.lower() == 'o':
                    Linha = Linha + '*'
                elif vogal.lower() == 'u':
                    Linha = Linha + '*'
                else:
                    Linha = Linha + vogal
            arquivo.write(Linha)
            linha = arquivo2.readline()

with open('arquivo_teste.txt', 'r') as arquivo:
    print(arquivo.read())
