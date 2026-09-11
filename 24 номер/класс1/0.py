f = open('24.1.класс.txt')
s = f.readline()
print(s)
maxlen = 0
nowlen = 0
for i in s:
    if i == 'B':
        nowlen += 1
    else:
        nowlen = 0
    if nowlen > maxlen:
        maxlen = nowlen
print(maxlen)