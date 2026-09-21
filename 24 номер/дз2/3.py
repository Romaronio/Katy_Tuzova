s = open('24.3.дз2.txt').readline()
n = 0
w = 0
l = 0
mini = 100000
for r in range(len(s)-3):
    if s[r] + s[r + 1] + s[r + 2] + s[r + 3] == '2025':
        n += 1
    if s[r] == 'W':
        w += 1
    while n > 110 or w > 90 or (s[l] != '2' and s[l] != 'W'):
        if s[l] + s[l + 1] + s[l + 2] + s[l + 3] == '2025':
            n -= 1
        if s[l] == 'W':
            w -= 1
        l += 1
    if n == 110 and w == 90 and (s[r] == '5' or s[r] == 'W') and r - l + 1 < mini:
        mini = r - l + 1
print(mini)