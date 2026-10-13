s = open('24_доп_дз_6.txt').readline()
t = 0
y = 0
l = 0
maxi = 0
for r in range(len(s)):
    if s[r] == '.':
        t += 1
    elif s[r] == 'Y':
        y += 1
    while t > 5 or y > 0:
        if s[l] == '.':
            t -= 1
        if s[l] == 'Y':
            y -= 1
        l += 1
    if t == 0 and y <= 5 and r - l + 1 > maxi:
        maxi = r - l + 1
print(maxi)