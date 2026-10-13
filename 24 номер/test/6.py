from re import *
s = open('24_6_итоговый_тест.txt').readline()
mass = []
num = '([1234][01234]*)'
reg = rf'({num}([*-]{num}|[*-]0)*)'
for i in finditer(reg, s):
    t = i.group()
    mass.append(t)
print(len(max(mass, key=len)))