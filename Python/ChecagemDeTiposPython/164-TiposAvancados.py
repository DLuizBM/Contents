'''
from typing import List, Tuple, Dict, Set

nomes: List[str] = ['Messi', 'Senna']
constants: Tuple[float] = 3.14, 2.71,
precos: Dict[str, float] = {'pneu': 400.00, 'filtro': 25.50}
conjunto: Set[int] = {1, 2, 3, 4, 5}

print(nomes)
print(constants)
print(precos)
print(conjunto)
print(__annotations__)

import random
I = [1, 2, 3, 4, 5]
J = [10, 20]
print(list(zip(I, J)))

set = list([(i, j) for j in J for i in I])
# o primeiro for executa primeiro
print(set)
random.shuffle(set)
print(set)

bar = list(range(1, 53))
print(bar[0:10:4])

alphabeto: dict = {"a": 1, "b": 2, "c": 3, "d": 4}
result = ' '.join(f"{k}{v}" for k, v in alphabeto.items())
print(result)


'''

import random
from typing import List, Tuple, Dict

#  https://www.alt-codes.net/suit-cards.php
NAIPES = '♠ ♡ ♢ ♣'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
CARTA = Tuple[str, str]
BARALHO = List[CARTA]

def criar_baralho(aleatorio: bool = False) -> BARALHO:
    """Cria um baralho com 52 cartas"""
    baralho: BARALHO = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho: BARALHO) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar() -> None:
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas: BARALHO = criar_baralho(aleatorio=True)
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    maos: Dict[str, BARALHO] = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
