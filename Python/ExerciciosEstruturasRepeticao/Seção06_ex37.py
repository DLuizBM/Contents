j = 0
lis = [0] * 10000
x = 0
y = 0
for num in range(1000, 10000):
    tot = num
    num = int(num / 1000)
    a = num
    a1 = num

    a = a * 1000

    b = tot - a
    b1 = b
    b = int(b / 100)
    b2 = b
    b = b * 100

    c = b1 - b
    c1 = c
    c = int(c / 10)
    c2 = c
    c = c * 10

    d = c1 - c

    #print(f"{a1}, {b2}, {c2}, {d}")

    if a1 > b2 and c2 > d:
        x = a1 + d
        y = c2 + b2
    elif a1 > b2 and c2 < d:
        x = a1 + c2
        y = d + b2
    elif a1 < b2 and c2 > d:
        x = b2 + d
        y = c2 + a1
    elif a1 < b2 and c2 < d:
        x = b2 + c2
        y = d + a1

    #print(f"{x}, {y}")

    if x > y or x == y:
        i = x * 10
        i = i + y
    elif y > x:
        i = y * 10
        i = i + x

    w = i*i

    if w == tot:
        lis[j] = w
        print(f"{a1}, {b2}, {c2}, {d}")
        j = j + 1

print(j)
for i in range(0, j):
    print(lis[i])

