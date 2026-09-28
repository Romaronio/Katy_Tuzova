from re import *
s = open('24_9_дз4.txt').readline()
num = '[12349][012349]*'
reg = f'{num}(([*-]{num})|([*-]0))*'
mas = []
for i in finditer(reg, s):
    i = i.group()
    # print(i)
    mas.append(i)
print(len(max(mas, key=len)))