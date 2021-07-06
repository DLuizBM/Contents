aq = input('Digite o nome do arquivo: ')
palavra = input('Digite a palavra a ser buscada: ')

cont = 0
with open(aq, 'r') as arquivo:
    linha = arquivo.readline()
    while linha:
        palavra_linha = ''
        for c in linha: # excluindo as vírgulas e '\n' da linha, para formar uma string sem ',' e '\n'
            if c != ',' and c != '\n':
                palavra_linha = palavra_linha + c
        for word in palavra_linha.split(): # transformando a string formada em uma lista de strings
            if palavra == word.lower():
                cont += 1
        linha = arquivo.readline()

print(f'O número de vezes que "{palavra}" foi repetida foi de: {cont}')



