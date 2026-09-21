s = open('24.2.дз2.txt').readline()
n = 0
ch = 0
maxi = 0
l = 0
for r in range(len(s)):
    if s[r] == 'F':
        n += 1
    if s[r] in '02468':
        ch += 1
    while n > 76 or ch > 1 or s[l] not in '02468':
        if s[l] == 'F':
            n -= 1
        if s[l] in '02468':
            ch -= 1
        l += 1
    if n == 76 and r - l + 1 > maxi:
        maxi = r - l + 1
print(maxi)