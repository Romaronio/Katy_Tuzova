from re import *
s = open('24_1_класс4.txt').readline().replace('*', 'A').replace('+', 'B')
mas = []
num = r'([1-9][0-9]*[02468]|[24680])'
reg = rf'{num}([AB]{num})+'
for i in finditer(fr'{reg}', s):
    t = i.group()
    mas.append(t)
print(len(max(mas, key=len)))