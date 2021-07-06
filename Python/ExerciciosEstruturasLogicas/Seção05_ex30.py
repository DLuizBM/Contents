print("Enter 3 integers.")
a = int(input())
b = int(input())
c = int(input())

x = 0
y = 0
z = 0

if a > b and a > c:
    x = a
elif b > a and b > c:
    x = b
elif c > a and c > b:
    x = c

if (a > b and a < c) or (a < b and a > c):
    y = a
elif (b > a and b < c) or (b < a and b > c):
    y = b
elif (c > a and c < b) or (c < a and c > b):
    y = c

if a < b and a < c:
    z = a
elif b < a and b < c:
    z = b
elif c < a and c < b:
    z = c

print(f"{x}, {y}, {z}.")
