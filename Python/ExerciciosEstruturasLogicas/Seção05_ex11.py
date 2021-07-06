print("Enter a integer!")
int1 = input('\n')
tam = len(int1)

int1 = int(int1)

if int1 <= 0:
    print("Invalid number.")
    exit()
elif tam == 1:
    print(f"{int1}")
elif tam == 2:
    a = int(int1/10)
    b = a * 10
    c = int1 - b
    tot = a + c
    print(f" The sum is {tot}")
elif tam == 3:
    a = int(int1/100)
    b = a * 100
    c = int1 - b
    d = int(c/10)
    e = int(d * 10)
    f = c - e
    print(f"The sum is {a+d+f}.")
