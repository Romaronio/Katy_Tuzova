f = open('24.3.класс.txt')
s = f.readline()
s = s.replace('ZXY', '*')
s = s.replace('ZYX', '*')
for i in s:
    if i != '*':
        s = s.replace(i, '#')
s = s.split('#')
print(max(s))