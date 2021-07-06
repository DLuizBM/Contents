"""
Escrevendo em arquivos

OBS: Ao abrir um arquivo para leitura, não podemos escrever, somente ler. Da mesma
forma que ao abrirmos um arquivo para escrita não podemos ler, apenas escrever.
-Função open() por padrão permite apenas a leitura

OBS: Ao abrir um arquivo para escrita, o arquivo é criado no SO. Se um arquivo já existir
e for aberto com 'w', ele é sobre escrito e o conteúdo anterior é perdido.


# Exemplo de escrita
with open('texto.txt', 'w') as arquivo:
    # w -> write: write recebe uma string como parâmetro, por isso não é possível
    # passar valor numérico
    arquivo.write('Flamengo Campeão da Libertadores 2019. \n')
    arquivo.write('Campeão Brasileiro de 2019. \n')

"""
# Recebendo dados do usuário

dado = input("Digite o nome do seu time: ")
with open('texto.txt', 'w') as arquivo:
    arquivo.write(f'{dado} é o melhor time!!')

