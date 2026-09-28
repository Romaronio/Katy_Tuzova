from re import *
s = open('24_9_дз4.txt').readline()
mas = []
for i in finditer(reg, s):
print(len(max(mas, key=len)))