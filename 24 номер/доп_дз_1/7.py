from re import *
s = open('24_доп_дз_7.txt').readline()
mas = []
reg = r'(([A-Z][a-z]*)( ([(A-Z)|(a-z)][a-z]*))*[.])'
for i in finditer(reg, s):
    t = i.group()
    mas.append(t)
str = max(mas , key=len)
print(str)
print(str.count(' ') + 1)