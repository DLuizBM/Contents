vx = []
vy = []

for _ in range(0, 5):
    num = int(input())
    vx.append(num)

for _ in range(0, 5):
    num = int(input())
    vy.append(num)

print(vx)
print(vy)

soma = [0] * 5
mul = [0] * 5
dif = [0] * 5
for i in range(0, 5):
    soma[i] = vx[i] + vy[i]
    mul[i] = vx[i] * vy[i]
    dif[i] = vx[i] - vy[i]

print(soma)
print(mul)
print(dif)



