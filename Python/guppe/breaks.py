"""
Break

utilizado para fazer paradas de maneira projetada
Para o loop

Continue para a iteração
"""

for numero in range(1, 11):
    if numero == 6:
        continue
    else:
        print(numero)

print("Saí do número")

while True:
    comando = input("Digite sair para sair:")
    if comando == "sair":
        break


