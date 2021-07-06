numero = int(input("Enter a integer.\n"))
i = 0
pair = 0
while numero != 1000:
    i = i + 1
    if numero % 2 == 0:
        print(f"This is a pair number.")
        pair = pair + 1
    numero = int(input("Enter a integer.\n"))

print(f"Number of numbers entered {i}.\n")
print(f"Number of pair numbers {pair}.\n")