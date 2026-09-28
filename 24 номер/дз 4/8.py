from re import *
s = open('24_8_дз4.txt').readline()
mas = []
reg = r'([A-Z]+[0-9]+[A-Z]+)'
for i in finditer(reg, s):
    t = i.group()
    mas.append(t)
print(len(max(mas, key=len)))