s = open('24_доп_дз_1.txt').readline()
x = 0
y = 0
l = 0
maxi = 0
for r in range(len(s)):
    if s[r] == 'X':
        x += 1
    elif s[r] == 'Y':
        y += 1
    while x > 1 or y > 1:
        if s[l] == 'X':
            x -= 1
        if s[l] == 'Y':
            y -= 1
        l += 1
    if x == 1 and y == 1 and r - l + 1 > maxi:
        maxi = r - l + 1
print(maxi)