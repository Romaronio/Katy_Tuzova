s = open('24_2_дз3.txt').readline()
n = 0
y = 0
l = 0
mini = 100000
for r in range(len(s) - 3):
    if s[r] + s[r + 1] + s[r + 2] + s[r + 3] == '2025':
        n += 1
    if s[r] == 'Y':
        y += 1
    while n > 60 or y > 120 or s[l] + s[l + 1] + s[l + 2] + s[l + 3] != '2025':
        if s[l] + s[l + 1] + s[l + 2] + s[l + 3] == '2025':
            n -= 1
        if s[l] == 'Y':
            y -= 1
        l += 1
    if n == 60 and y == 120 and r - l + 1 < mini: #and (s[r] == '5' or s[r] == 'Y'):
        mini = r - l + 1
print(mini)