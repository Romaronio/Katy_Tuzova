f = open('24.8.класс.txt')
s = f.readline()
n = 0
nmax = 0
s = s.replace('XZZY', '*')
for i in s:
    if i != '*':
        n += 1
    else:
        n = 0
    if n > nmax:
        nmax = n
print(nmax)