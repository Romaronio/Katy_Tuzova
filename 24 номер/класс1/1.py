f = open('24.2.класс.txt')
s = f.readline()
n = 0
maxn = 0
for i in s:
    if i in 'EIO':
        s = s.replace(i, '*')
    else:
        s = s.replace(i, '#')
s = s.replace('#*', 'A')
s = s.replace('*', '#')
s = s.split('#')
print(max(s))

