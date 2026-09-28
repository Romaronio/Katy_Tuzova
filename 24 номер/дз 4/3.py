s = open('24_3_дз4.txt').readline()
for i in 'AEIOUY':
    s = s.replace(i, '*')
for i in 'BCDFGHJKLMNPQRSTVWXZ':
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