from re import *
s = open('24_4_класс4.txt').readline()
reg = '[1-9]|[AB]([1-9]|[AB])+'
mas = []
for i in finditer(reg, s):
    t = i.group()
    mas.append(t)
print(len(max(mas, key=len)))