s = open('24_4_итоговый_тест.txt').readline()
n = 0
y = 0
l = 0
maxi = 0
for r in range(len(s)):
    if s[r - 3] + s[r - 2] + s[r - 1] + s[r] == '2025':
        n += 1
    if s[r] == 'Y':
        y += 1
    while n > 50:
        if s[l] + s[l + 1] + s[l + 2] + s[l + 3] == '2025':
            n -= 1
        if s[l] == 'Y':
            y -= 1
        l += 1
    if y >= 140 and n == 50 and s[r - 3] + s[r - 2] + s[r - 1] + s[r] == '2025' and r - l + 1 > maxi:
        maxi = r - l + 1
print(maxi)