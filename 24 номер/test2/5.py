s = open('24_5.txt').readline()
n = 0
mini = 1000000
l = 0
rr = 0
ll = 0
for r in range(len(s)):
    if s[r - 2] + s[r - 1] + s[r] == 'ABC':
        n += 1
    while n > 110 or s[l] != 'A':
        if s[l] + s[l + 1] + s[l + 2] == 'ABC':
            n -= 1
        l += 1
    if r - l + 1 < mini and n == 110 and s[r] == 'C' and s[l] == 'A':
        mini = r - l + 1
        rr = r
        ll = l
print(mini)
print(s[ll:rr+1].count('ABC'))