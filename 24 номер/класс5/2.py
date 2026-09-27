from re import *
s = open('24_2_класс5.txt').readline()
mas = []
num = r'([1-9][0-9]*|0)'
reg = rf'(({num}\*)*0(\*{num})*)'
reg1 = rf'({reg}(\+{reg})*)'
for i in finditer(reg1, s):
    t = i.group()
    mas.append(t)
print(len(max(mas, key=len)))