
conj1 = {0}
conj2 = {0}

for _ in range(0, 3):
    num = int(input())
    conj1.add(num)
    num1 = int(input())
    conj2.add(num1)

conj1.remove(0)
conj2.remove(0)
print(conj1)
print(conj2)

conj3 = conj2.intersection(conj1)
print(list(conj3))