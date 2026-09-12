s = open('24.4.класс2.txt').readline()
# s = s.split('AXMM')
# print(len(max(s, key=len)) + 6)
l = 0
k = 0
n = 0
t = 0
m = 0
for r in range(len(s)-3):
    if s[r] + s[r+1] + s[r+2] + s[r+3] == 'AXMM':
        k += 1
    while k > 0:
        if s[l] + s[l+1] + s[l+2] + s[l+3] == 'AXMM':
            k -= 1
        l += 1
    m = max(m, r-l)
    n = l
    t = r
print(s[n:t+6])
print(s[n:t+6].count('AXMM'))
print(m)
