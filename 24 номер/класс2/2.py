s = open('14.09.26/24.2.класс2.txt').readline()
for i in 'AEIOUY':
    s = s.replace(i, 'A')
l = 1
k = 0
a = 0
n = 0
t = 0
m = 10000000
for r in range(len(s)-1):
    if s[r] == '2' and s[r+1] == '0':
        k += 1
    if s[r] == 'A':
        a += 1
    while k > 26 or a > 1 or s[l] != '2':
        if s[l] + s[l + 1] == '20':
            k -= 1
        if s[l] == 'A':
            a -= 1
        l += 1
    if k == 26 and s[r] == 'A':
        m = min(m, r-l+1)
        n = l
        t = r
print(s[n:t+1])
print(s[n:t+1].count('20'))
print(m)

