from re import *
s = open('24_6_дз4.txt').readline()
reg = r'(([18]{2}[DR])+)'
mas = []
for i in finditer(reg, s):
    t = i.group()
    mas.append(t)
print(len(max(mas, key=len)) // 3)