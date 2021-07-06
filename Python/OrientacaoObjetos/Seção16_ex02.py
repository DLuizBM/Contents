"""
Comandos que poderiam ser usados

# lista = [Agenda('Alonso'), Agenda('Hamilton')]
# print(lista[0].getname())
# dic = {'Alonso': Agenda('Alonso'), 'Senna': Agenda('Senna')}
# print(dic['Alonso'].getname())

# for chave, valor in enumerate(dic): # enumarate em dic, devolve a posição(index) de cada item no dicionário
#   print(chave)
#   print(valor)


"""


class Agenda:

    contador = 1

    def __init__(self, nome, idade, altura):
        if Agenda.contador <= 3:    # fazer ess tipo de verificação após o método construtor
            self.__nome = nome
            self.__idade = idade
            self.__altura = altura
            Agenda.contador += 1
            print('Cadastro salvo com sucesso')
        else:
            print(f'Limite de cadastros na agenda atingido, o máximo permitido é 3. ', end='')
            print(f'Exclua usuários para fazer novos cadastros.')

    def getname(self):
        return self.__nome

    def removeperson(self):
        Agenda.contador -= 1
        del self

    def dados(self):
        print(f'Nome: {self.__nome}\nIdade: {self.__idade}\nAlura: {self.__altura}.')


dic_agenda = {}
print('1 - Cadastro')
print('2 - Remover pessoa')
print('3 - Buscar pessoa')
print('4 - Imprimir todos os dados da agenda')
print('5 - Imprimir dados de uma pessoa')
print('6 - Encerrar busca')
print('')
opcao = int(input('Escolha uma das opções acima: '))
print('')

while opcao != 6:
    if opcao == 1:
        nome = input('Digite o nome da pessoa que deseja cadastra na agenda: ')
        idade = int(input('Digite a idade: '))
        altura = float(input('Digite a altura: '))

        novo = {nome: Agenda(nome, idade, altura)}
        dic_agenda.update(novo)
    elif opcao == 2:
        temp = ''
        pessoa = input('Digite o nome da pessoa que deseja excluir: ')
        for chave in dic_agenda.keys():
            if chave == pessoa:
                temp = chave

        if temp:
            dic_agenda[temp].removeperson()
            dic_agenda.pop(temp)   # pop remove o item especificado do dicionário
            print('Pessoa excluída com sucesso.')
            print('')
        else:
            print('Essa pessoa não está cadastrada.')
            print('')
        if not dic_agenda:
            print('A agenda está vazia!')
            print('')
    elif opcao == 3:
        temp = ''
        pessoa = input('Digite o nome da pessoa que deseja buscar: ')
        for chave in dic_agenda.keys():
            if chave == pessoa:
                temp = chave
        if pessoa:
            print('Essa pessoa está cadastrada.')
            print('')
        else:
            print('Esse pessoa não está cadastrada.')
            print('')
        if not dic_agenda:
            print('A agenda está vazia.')
            print('')
    elif opcao == 4:
        if not dic_agenda:
            print('A agenda está vazia.')
            print('')
        else:
            (list(map(lambda cadastros: dic_agenda[cadastros].dados(), dic_agenda.keys())))
            # passando para cadastros as chaves: acessando cada valor do dicionário(um objeto) pela chave e
            # chamando o métodos dados()
            print('')
    elif opcao == 5:
        pessoa = input('Digite o nome da pessoa que deseja buscar: ')
        busca = list(filter(lambda x: pessoa == x, dic_agenda.keys()))
        if not dic_agenda:
            print('A agenda está vazia.')
            print('')
        elif bool(busca):   # list(filter) retorna uma lista, se a lista estiver com algum valor retorna booleano true
            print(f'Pessoa encontrada com sucesso')  # se estiver vazia, retorna o valor booleno false
            posicao = 0
            for chave, valor in enumerate(dic_agenda):
                if valor == pessoa:
                    posicao = chave
            print(f'Essa pessoa está na posição {posicao + 1} da agenda.')
            dic_agenda[pessoa].dados()
            print('')
        elif not bool(busca):
            print('Pessoa não encontrada.')
            print('')

    print('1 - Cadastro')
    print('2 - Remover pessoa')
    print('3 - Buscar pessoa')
    print('4 - Imprimir todos os dados da agenda')
    print('5 - Imprimir dados de uma pessoa')
    print('6 - Encerrar busca')
    print('')
    opcao = int(input('Escolha uma das opções acima: '))
    print('')

