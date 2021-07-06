with open('arquivo_referencia.txt', 'r') as arquivo2:
    with open('arquivo_teste.txt', 'w') as arquivo:
        linha = arquivo2.readline()
        while linha:
            arquivo.write(linha)
            linha = arquivo2.readline()

carac = input("Digite um caractere para saber quantas vezes ele se repetiu: ")
quantidade = 0
with open('arquivo_teste.txt') as arquivo:
    linha = arquivo.readline()
    while linha:
        res = list(filter(lambda c: c.lower() == carac.lower(), linha))
        quantidade += len(res)
        linha = arquivo.readline()

print(quantidade)
