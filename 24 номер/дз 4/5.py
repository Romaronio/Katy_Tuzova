from re import *
s = open('24_5_дз4.txt').readline()
reg = r'([123456789ABCD][0123456789ABCD]*)'
mas = []
for i in finditer(reg, s):
    t = i.group()
    mas.append(t)
print(len(max(mas, key=len)))