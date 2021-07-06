print("Enter two grades.")

nota1 = float(input('\n'))
if nota1 < 0:
    print(f"{nota1} is not a valid value.")
    exit()

nota2 = float(input('\n'))
if nota2 < 0:
    print(f"{nota2} is not a valid value.")
    exit()

print(f"The avarage grade is {(nota2+nota1)/2}.")


