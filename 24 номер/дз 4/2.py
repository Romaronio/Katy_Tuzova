# from re import *
# s = open('24_2_дз4.txt').readline()
# for i in '02468':
#     s = s.replace(i, '*')
# for i in '13579':
#     s = s.replace(i, '#')
# reg = r'((*){0-1}(#*)*(#){0-1})'
# mas = []
# for i in finditer(reg, s):
#     t = i.group()
#     mas.append(t)
# print(len(max(mas, key=len)))

s = open('24_2_дз4.txt').readline()
for i in '02468':
    s = s.replace(i, '*')
for i in '13579':
    s = s.replace(i, '#')
n = 0
maxi = 0
c = 0
for i in s:
    if i != c:
        n += 1
        c = i
    else:
        n = 1
        c = i
    if n > maxi:
        maxi = n
print(maxi)