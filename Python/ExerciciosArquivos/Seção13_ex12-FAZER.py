nome = input('Entre com o nome: ')
telefone = input('Entre com o telefone: ')
cadastro = []
while telefone != '0':
    cadastro.append(nome + ': ' + telefone + '.' + '\n')
    nome = input('Entre com o nome: ')
    telefone = input('Entre com o telefone: ')

with open('arquivo_teste2.txt', 'w') as arquivo:
    for escreve in cadastro:
        arquivo.write(escreve)

