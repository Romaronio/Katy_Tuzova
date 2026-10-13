s = open('24_4.txt').readlines()
n = 0
k = 0
mass = []
for st in s:
    for i in range(len(st)):
        if st[i - 3] + st[i - 1] + st[i] == 'ZRO':
            n += 1
    if n > 0:
        k += 1
    n = 0
print(k)

from re import*
s2 = open('24_4.txt').readlines()
mass = []
k2 = 0
reg = r'(Z[A-Z]RO)'
for st in s2:
    for i in finditer(reg, st):
        t = i.group()
        mass.append(t)
    if len(mass) > 0:
        k2 += 1
    mass = []
print(k2)