s = open('24_6.txt').readline()
n = 0
l = 0
maxi = 0
ll = 0
for r in range(len(s)):
    if s[r] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        n += 1
    while n > 2 or s[l] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if s[l] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            n -= 1
        l += 1
    if r - l + 1 > maxi and n == 2 and s[r] == s[l]:
        maxi = r - l + 1
        ll = l
print(ll)

from re import*
s2 = open('24_6.txt').readline()
mass = []
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    reg = rf'(({i})[0-9]*({i}))'
    for ii in finditer(reg, s2):
        t = ii.group()
        mass.append(t)
m = max(mass, key=len)
s2 = s2.replace(str(m), '*')
nn = 0
for i in s2:
    if i != '*':
        nn += 1
print(nn + 1)

