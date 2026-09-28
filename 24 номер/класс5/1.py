from re import *
s = open('24_1_класс5.txt').readline()
mas = []
num = r'[1-4][0-4]*'
reg = rf'{num}([*-]{num}|[*-]0)*'
for i in finditer(reg, s):
    t = i.group()
    mas.append(t)
print(len(max(mas, key=len)))