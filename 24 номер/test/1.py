s = open('24_1_итоговый_тест.txt').readline()
for i in 'AEIOUY':
    s = s.replace(i, '*')
for i in 'BCDFGHJKLMNPQRSTVWXZ':
    s = s.replace(i, '#')
n = 0
maxi = 0
sim = 0
for i in s:
    if i != sim:
        n += 1
        sim = i
    else:
        n = 1
    if n > maxi:
        maxi = n
print(maxi)

# s = open('24_1_итоговый_тест.txt').readline()
# for i in 'AEIOUY':
#     s = s.replace(i, '*')
# for i in 'BCDFGHJKLMNPQRSTVWXZ':
#     s = s.replace(i, '#')
# from re import *
# mass = []
# reg = r'((/*){0-1}(#/*)*(#){0-1})'
# for i in finditer(reg, s):
#     t = i.group()
#     mass.append(t)
# print(len(max(mass, key=len)))
# print(max(mass, key=len))