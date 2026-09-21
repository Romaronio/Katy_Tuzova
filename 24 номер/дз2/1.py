s = open('24.1.дз2.txt').readline()
l = 0
n = 0
maxi = 0
for r in range(len(s) - 1):
    if s[r] + s[r + 1] == 'BC':
        n += 1
    while n > 180:
        if s[l] + s[l + 1] == 'BC':
            n -= 1
        l += 1
    if r - l + 2 > maxi:
        maxi = r - l + 2
print(maxi)