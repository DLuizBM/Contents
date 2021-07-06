"""
Leitura de arquivos

- Para abrir um arquivo, basta usar a funçõa integrada open()
- open() -> na forma mais simples de utilização, passamos apenas o nome/caminho do arquivo.
Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos.

OBS: por padrão a função open() abre o arquivo para leitura. Se o arquivo não existir
o FileNotFoundError será apresentado

"""

arquivo = open('texto.txt')
print(arquivo)
# Saída: <_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>
# mode = 'r' - modo de leitura('r' -> read()) - modo padrão
# UTF-8 -> todos os caracteres especiais serão reconhecidos pelo programa

# Para realizar a leitura deve-se usar a função read()
print(arquivo.read())
# Saída: olá mundo
# OBS: o python utiliza um recurso chamado cursor, para trabalhar com arquivos.
# Esse cursor funciona como o cursor quando estamos escrevendo. Se for chamado
# um segundo print(arquivo.read()), não será impresso novamente o conteúdo do arquivo
# pois quando se lê um arquivo a primeira vez, o cursor para na próxima linha após o arquivo(linha vazia)
# dessa forma, nada será impresso.
# A função read() lê todo o conteúdo do arquivo e não linha por linha
# A função read() - retorna uma string