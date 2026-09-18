from re import *
s = open('24.1.класс.txt').readline()
mas = []
reg = r'[B]*'
for i in finditer(reg, s):
    t = i.group()
    mas.append(t)
print(len(max(mas, key=len)))
