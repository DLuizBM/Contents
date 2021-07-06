
num = int(input("Enter a integer. \n"))
lis = [0] * num
i = 0
print(lis)
for _ in range(0, num):
    n = int(input())
    lis[i] = n
    i = i + 1

maior = int(max(lis))

i = 0
j = 0

for _ in range(0, num):
    if maior == lis[i]:
        j = j + 1
    i = i + 1

print(f"{maior}, {j}")
