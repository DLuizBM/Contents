"""
Erros mais comuns

1 - SyntaxError: Algo escrito que o python não reconhece como parte da linguagem

# Exemplo

- def funcao: # falta o parênteses na função
    print('Olá mundo')

- def = 1 # palavra reservada não pode ser usada como variável

2 - NameError -> Ocorre quando uma variável ou função não foi definida

- print(numero) # Número não foi definido
- Quando função é chamada e não foi definida
- Erro no uso de variáveis globais e locais
    a = 18
    if a < 10: # se a > 10, entra na condição, cria-se a variável msg e printa, mas o python reclama
        msg = 'Olá mundo'
    print(msg) # não vai entrar nessa linha, já que a condição do if não será cumprida

3 - TypeError -> Ocorre quando uma operação é aplicada a um tipo errado
- Soma de string com int, por exemplo
    print(2 + 'abc')
- Aplicação de função a tipo errado
    a = 18
    print(len(a)) # len não é aplicado a inteiros

4 - IndexError -> Ocorre quando se usa um índice inválido para acessar um elemento de uma coleção
- Lista = [0, 1]
    print(Lista[2]) # não existe posição 2

- lista = ['geek']
    print(lista[0][10]) # não existe letra na posição 10, a última posição de letra é a 3


5 - ValueError -> Ocorre quando uma função/operação built-in recebe um argumento  com tipo
correto, mas valor inapropriado

- print(int('ss')) # o cast para converter para int espera receber uma string, mas o
passado ,'ss', não pode ser convertido, logo, o tipo está certo, mas o valor não

6 - KeyError -> Ocorre quando tentamos acessar a chave em um dicionário, mas essa chave
não existe
- dic = {'a': 1, 'b':2}
    print(dic['c']) # chave inexistente

7 - AttributeError -> Ocorre quando uma variável não atributo/função
- tupla = (23, 4, 5, 6, 1)
    print(tupla.sort()) # gera erro de atributo, pois sort() é uma função de lista

8 - IndentationError -> Ocorre quando não é respeitado a identação do python (4 espaços)
- def nova():
  print("olá mundo") # necessário os 4 espaços

OBS: Exceptions e Errors, são sinônimos.
"""

a = 18
if a > 10:
    msg = 'Olá mundo'
print(msg)  # não vai
