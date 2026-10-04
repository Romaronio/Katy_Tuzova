s = open('24_доп_дз_4.txt').readline()
for i in 'ABCD':
    s = s.replace(i, '*')
n = 0
l = 0
maxi = 0
for r in range(len(s)):
    if s[r - 2] + s[r - 1] + s[r] == '***':
        n += 1
    while n > 0:
        if s[l] + s[l + 1] + s[l + 2] == '***':
            n -= 1
        l += 1
    if n == 0 and r - l + 1 > maxi:
        maxi = r - l + 1
print(maxi)