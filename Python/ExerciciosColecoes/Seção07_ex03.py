
A = []

for _ in range(0, 10):
    num = int(input())
    A.append(num)
print(A)

B = []

for num in range(0, 10):
    a = A[num] * A[num]
    B.append(a)
print(B)
