
n = int(input("Enter a positive integer. \n"))
h = 1
fat = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        fat = fat * j
        print(f"{fat} \n")

    h = h + 1/fat
    fat = 1

print(h)