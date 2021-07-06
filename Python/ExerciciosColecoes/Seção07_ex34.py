from collections import deque

vet = []

for _ in range(0, 5):
    num = int(input("Enter a integer: "))
    if num in vet:
        while num in vet:
            print("This already exist in vector, please enter another numbe: ")
            num = int(input())
    vet.extend([num])


print(vet)