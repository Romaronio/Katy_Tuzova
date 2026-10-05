s = open('24_7.txt').readline()
y = 0
n = 0
l = 0
maxi = 0
for r in range(len(s)):
    if s[r - 3] + s[r - 2] + s[r - 1] + s[r] == '2025':
        n += 1
    if s[r] == 'Y':
        y += 1
    while y > 80:
        if s[l] + s[l + 1] + s[l + 2] + s[l + 3] == '2025':
            n -= 1
        if s[l] == 'Y':
            y -= 1
        l += 1
    if r - l + 1 > maxi and y == 80 and n >= 90:
        maxi = r - l + 1
print(maxi)