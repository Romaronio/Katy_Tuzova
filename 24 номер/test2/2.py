s = open('24_2.txt').readline()
n = 0
maxi = 0
for i in s:
    if i in '0123456789':
        n += 1
    else:
        n = 0
    if n > maxi:
        maxi = n
print(maxi)

from re import*
s2 = open('24_2.txt').readline()
mass = []
reg = r'([0-9]+)'
for i in finditer(reg, s2):
    t = i.group()
    mass.append(t)
print(len(max(mass, key=len)))