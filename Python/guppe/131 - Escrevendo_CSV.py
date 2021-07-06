"""
Escrendo em arquivos CSV

# Método writer()
O método writer() cria um objeto que permite que seja possível escrever em CSV
writerow() -> escreve uma linha

# Método DictWriter()
OBS: As chaves no dicionário, devem ser as mesmas utilizadas no cabeçalho

# WRITER

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    # w reescreve o arquivo, apagando as informações já existentes
    # para continuar escrevendo no arquivo sem apagar, usa-se 'a'
    escritor = writer(arquivo)
    filme = ''
    escritor.writerow(['Título', 'Genêro', 'Duração'])
    # essa linha cria o cabeçalho, como writerow trabalha com lista, deve-se escrever
    # cada linha dessa forma
    while filme != 'sair':
        filme = input('Nome do filme')
        if filme != 'sair':
            genero = input('Informe o gênero')
            duracao = input('Duração do filme')
            escritor.writerow([filme, genero, duracao])

"""

# DICTWRITER

from csv import DictWriter

with open('filmes.csv', 'w') as arquivo:
    cabecalho = ['titulo', 'genero', 'duração']
    escritor = DictWriter(arquivo, fieldnames=cabecalho)
    escritor.writeheader()
    # o cabeçalho é criado com o writeheader()
    filme = ''
    while filme != 'sair':
        filme = input('Nome do filme')
        if filme != 'sair':
            genero = input('Informe o gênero')
            duracao = input('Duração do filme')
            escritor.writerow({'titulo': filme, 'genero': genero, 'duração': duracao})
            # writerow(), escreve a linha
