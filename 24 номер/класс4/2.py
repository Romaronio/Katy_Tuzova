from re import *
s = open('24.2.класс.txt').readline()
reg = r'((ZYX)|(ZXY))*'
mas = []
for i in finditer(reg, s):
    t = i.group()
    mas.append(t)
print(max(mas, key=len))
print(len(max(mas, key=len)) // 3)

