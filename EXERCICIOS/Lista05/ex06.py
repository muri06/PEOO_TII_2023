A1 = int(input())
A2 = int(input())
A3 = int(input())

t1 = A2 * 2 + A3 * 4
t2 = A1 * 2 + A3 * 2
t3 = A1 * 4 + A2 * 2

if t1 <= t2:
    menor = t1
else:
    menor = t2
if menor >= t3:
    menor = t3
print(menor)
