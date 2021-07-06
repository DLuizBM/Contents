
with open('arquivo_referencia.txt', 'r') as arquivo2:
    with open('arquivo_teste.txt', 'w') as arquivo:
        linha = arquivo2.readline()
        while linha:
            arquivo.write(linha)
            linha = arquivo2.readline()
            
vogais = []
with open('arquivo_teste.txt') as arquivo:
    for linha in arquivo:
        for vogal in linha:
            if vogal.lower() == 'a':
                vogais.append(vogal)
            elif vogal.lower() == 'e':
                vogais.append(vogal)
            elif vogal.lower() == 'i':
                vogais.append(vogal)
            elif vogal.lower() == 'o':
                vogais.append(vogal)
            elif vogal.lower() == 'u':
                vogais.append(vogal)
print(vogais)
print(f'O número de vogais nesse texto é de: {len(vogais)}')
