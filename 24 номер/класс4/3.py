from re import *
s = open('24_3_класс4.txt').readline()
reg = r'([BC]{2}A)+'
mas = []
for i in finditer(reg, s):
    t = i.group()
    mas.append(t)
print(len(max(mas, key=len)))
print(max(mas, key=len))
print(mas)