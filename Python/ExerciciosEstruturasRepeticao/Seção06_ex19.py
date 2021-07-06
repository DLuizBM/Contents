numero1 = input("Enter a number between 100 and 999.\n")
numero = int(numero1)
if numero < 100 or numero > 999:
    while numero < 100 or numero > 1000:
        print("Please enter a number between 100 and 999.")
        numero1 = input()
        numero = int(numero1)
    lis = list(numero1) # separa caractere da string em uma posição  na lista
    for i in range(0, 3):
        print(lis[i])
else:
    lis = list(numero1)
    for i in range(0, 3):
        print(lis[i])
