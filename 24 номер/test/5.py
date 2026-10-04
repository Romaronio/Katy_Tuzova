s = open('24_5_итоговый_тест.txt').readline()
n = 0
maxi = 0
l = 0
for r in range(len(s)):
    if s[r - 3] + s[r - 2] + s[r - 1] + s[r] == 'FSRQ':
        n += 1
    while n > 80:
        if s[l] + s[l + 1] + s[l + 2] + s[l + 3] == 'FSRQ':
            n -= 1
        l += 1
    if n == 80 and r - l + 1 > maxi:
        maxi = r - l + 1
print(maxi)