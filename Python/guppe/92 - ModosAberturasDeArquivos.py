"""
Modos de aberturas de arquivos

r -> abre para leitura - padrão
w -> abre para escrita - sobreescreve caso o arquivo já esxista
x -> abre para escrita somente se o arquivo não existir. Se já existir gera erro
a -> abre para escrita, adicionando o conteúdo ao final do arquivo, se não existir o arquivo ele cria
+ -> abre para o módulo de atualização, temos o controle do cursor, mas a+, não tem o controle


# Exemplo 'x'
with open('texto2.txt', 'x') as arquivo:
    arquivo.write('Teste de arquivo \n')
# Não apresenta problema

with open('texto2.txt', 'x') as arquivo:
    arquivo.write('Teste de arquivo \n')
# Saída: FileExistsError: [Errno 17] File exists: 'texto2.txt'


# Exemplo 'a'

with open('texto.txt', 'a') as arquivo:
    arquivo.write('\n')
    while True:
        time = input("Digite o nome do jogador: ")
        if time != 'sair':
            arquivo.write(time + '\n')
        else:
            break


# Adicionando no início do arquivo

with open('texto.txt', 'a') as arquivo:
    arquivo.seek(0)
    arquivo.write('Qual o melhor time? \n')
# mesmo com seek() isso não é posśivel abrindo com 'a', pois não controlamos o cursor

"""

# Lógica para adicionar no topo

with open('texto2.txt', 'r+') as arquivo:
    texto = 'Agora consegui adicionar no topo sim 2 \n'
    print(texto)
    arquivo.seek(0)
    arquivo.write(texto)
# Dessa forma é possível adicionar no início, mas o r+ substitui a linha

