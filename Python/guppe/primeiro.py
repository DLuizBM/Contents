
def func1():
    print(f'Flamengo Campeão!!')


if __name__ == '__main__':
    func1()
    print('Primeiro está sendo executado diretamente.')
else:
    print('Primeiro foi importado.')
    print(f'{__name__}')

# Colocar essa verificação de __name__ evita o problema de print duplo, como aconteceu
# em um dos exemplos, lembrar que o else não é necessário.
# o if verifica se o módulo está sendo executado diretamente, se sim, execute as funções
# se não, não faça nada
# Se executado diretamente, o __name__ possui o valor __main__, mas
# se for só importado recebe como valor o nome do arquivo sem extensão __name__ = primeiro