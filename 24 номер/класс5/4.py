from re import *
s = open('24_4_класс5.txt').readline()
reg = r'(([12]{2}[AB])*)'
mas = []
for i in finditer(reg, s):
    t = i.group()
    mas.append(t)
print(len(max(mas, key=len)) / 3)