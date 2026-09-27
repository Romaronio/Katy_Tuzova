from re import *
s = open('24_3_класс5.txt').readline()
num = r'([6789][06789]*)'
reg = rf'({num}([*-]{num}|[*-]0)*)'
mas = []
for i in finditer(reg, s):
    t = i.group()
    mas.append(t)
print(len(max(mas, key=len)))