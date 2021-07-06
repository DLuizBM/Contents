"""
Módulo Random e o que são módulos.
- Em python, módulos nada mais são do que outros arquivos python
- Módulo random -> possui várias funções para geração de números pseudo-aleatórios(pode haver repetição)


# OBS: existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - importando todo o módulo (não recomendado)

import random
# ao realizar o import de todo o módulo,todas as funções, atributos, classes e
# propriedades que estiverem dentro do módulo ficarão disponíveis (ficarão em memória)

# função random() gera um número pseudo-aleatório de 0 a 1

print(random.random())
# não confundir o pacote com a função


# Forma 2 - importando uma função específica do módulo
# forma recomendada

from random import random
for i in range(0, 10):
    print(random())

# uniform() -> gera números pseudo-aleatórios(ponto flutuante) entre um valor estabelecida

from random import uniform
for _ in range(0, 10):
    print(uniform(3, 7)) # o 7 não está incluído

# randint() -> gera número pseudo-aleatório(inteiros) entre um valor estabelecido
from random import randint

for _ in range(0, 10):
    print(randint(1, 10))


# choice() -> mostra um valor aleatório entre um iterável

# Exemplo - Pedra, papel e tesousa
from random import choice

ppt = ['pedra', 'papel', 'tesoura']
escolha = 'pedra'

while escolha != ' ':
    print("Escolha 1 para pedra, 2 para papel, 3 para tesoura:")
    escolha = input()

    # computador jogando
    a = choice(ppt)

    if escolha == '1':
        if a == 'pedra':
            print("Empate.")
        elif a == 'papel':
            print("Papel enrola pedra, você perdeu!")
        else:
            print("Você ganhou!")
    elif escolha == '2':
        if a == 'pedra':
            print("Papel enrola pedra, você ganhou!")
        elif a == 'papel':
            print("Empate.")
        else:
            print("Tesoura corta papel, você perdeu!")
    else:
        if a == 'pedra':
            print("Pedra quebra tesoura, você perdeu!")
        elif a == 'papel':
            print("Tesoura corta pape, você ganhou")
        else:
            print("Empate.")

print(choice('Ayrton Senna'))

"""
# shuffle() -> tem a função de embaralhar dados
from random import shuffle

lista = [1, 2, 3, 4]

shuffle(lista)
print(lista)