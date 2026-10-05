s = open('24_3.txt').readline()
s = s.replace('XYZ', '*')
print(s)
n = 0
maxi = 0
for i in s:
    if i == '*':
        n += 3
    else:
        n = 0
    if n > maxi:
        maxi = n
print(maxi)

from re import*
s2 = open('24_3.txt').readline()
mass = []
reg = r'((XYZ)+)'
for i in finditer(reg, s2):
    t = i.group()
    mass.append(t)
print(len(max(mass, key=len)))