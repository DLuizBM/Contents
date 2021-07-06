class Elevador:
    andar = 0
    pessoas = 0

    def __init__(self, num_pessoas, num_andares):
        self.__num_pessoas = num_pessoas
        self.__num_andares = num_andares
        self.__terreo = 0

    def sobe_andar(self):
        if Elevador.andar < self.__num_andares:
            Elevador.andar += 1
        else:
            print('O elevador já está no último andar.')
            print('')

    def desce_andar(self):
        if Elevador.andar != self.__terreo and Elevador.andar > 0:
            Elevador.andar -= 1
        elif Elevador.andar == self.__terreo:
            print('O elevador está no térreo.')
            print('')

    def entra_pessoa(self):
        if Elevador.pessoas < self.__num_pessoas:
            Elevador.pessoas += 1
        else:
            print('O elevador já está com o número máximo de pessoas.')
            print('')

    @classmethod    # 'poderia' ser um método estático, mas como está utilizando o atributo de classe pessoas
    def sai_pessoa(cls):    # deve-se colocar como método de classe
        if cls.pessoas > 0:
            cls.pessoas -= 1
        else:
            print('Não há pessoas no elevador')
            print('')

    def getfloor(self):
        if Elevador.andar != self.__terreo:
            print(f'O elevador está no {Elevador.andar}º andar.')
        elif Elevador.andar == self.__terreo:
            print('O elevador está no térreo.')

    @classmethod
    def getpeople(cls):
        if cls.pessoas != 0 and cls.pessoas > 0:
            print(f'O elevador está com {cls.pessoas} pessoas.')
        elif cls.pessoas == 0:
            print(f'O elevador está vazio.')


elevador1 = Elevador(18, 30)

print('1 - Sobe andar.')
print('2 - Desce andar.')
print('3 - Entra pessoa.')
print('4 - Sai pessoa.')
print('5 - Encerrar.')
opcao = int(input('Escolha uma das opções: '))

while opcao != 5:
    if opcao == 1:
        elevador1.sobe_andar()
        elevador1.getfloor()
    elif opcao == 2:
        elevador1.desce_andar()
        elevador1.getfloor()
    elif opcao == 3:
        elevador1.entra_pessoa()
        Elevador.getpeople()
    elif opcao == 4:
        Elevador.sai_pessoa()
        Elevador.getpeople()
    print('')

    print('1 - Sobe andar.')
    print('2 - Desce andar.')
    print('3 - Entra pessoa.')
    print('4 - Sai pessoa.')
    print('5 - Encerrar.')
    opcao = int(input('Escolha uma das opções: '))
