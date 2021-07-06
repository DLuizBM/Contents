
numero = int(input("Enter a number!"))
i = 0

if numero % 2 == 0:
    numero = numero + 1
    while i == 0:
        print(f"{numero} \n ")
        numero = numero + 2


if numero % 2 != 0:
    while i == 0:
        numero = numero + 2
        print(f"{numero} \n")
