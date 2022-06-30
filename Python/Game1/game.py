from models.calcular import Calcular

def main() -> None:
    pontos: int  = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade [1, 2, 3 ou 4]: \n'))

    calcular: Calcular = Calcular(dificuldade=dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calcular.mostrar_operacao()

    resultado: int = int(input(''))

    if calcular.checar_resultado(resultado):
        pontos += 1
        print(f"Você tem {pontos} pontos.")
    
    continuar: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não]: \n'))

    if continuar:
        jogar(pontos)
    else:
        print(f"Você finalizou com {pontos} pontos.")

if __name__ == '__main__':
    main()