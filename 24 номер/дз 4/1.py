s = open('24_1_дз4.txt').readline()
n = 0
l = 0
maxi = 0
for r in range(len(s)):
    if s[r] == 'F':
        n += 1
    while n > 1:
        if s[l] == 'F':
            n -= 1
        l += 1
    if r - l + 1 > maxi:
        maxi = r - l + 1
print(maxi)