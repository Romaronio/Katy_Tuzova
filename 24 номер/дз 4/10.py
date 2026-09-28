from re import *
s = open('24_10_дз4.txt').readline()
mas = []
num = '([123456789][0123456789]*)'
reg = rf'({num}([*-]{num})*)'
for i in finditer(reg, s):
    t = i.group()
    mas.append(t)
print(len(max(mas, key=len)))