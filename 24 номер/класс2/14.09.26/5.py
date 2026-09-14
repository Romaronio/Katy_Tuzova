s = open('24_5_класс3.txt').readline()
s = s.replace('XX', '*')
s = s.replace('YY', '#')
s = s.replace('ZZ', '@')
k = 0
now = 0
maxi = 0
rr = 0
ee = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        if now > maxi:
            maxi = max(maxi, now)
            rr = i
            ee = i - now
        now = 0
    if s[i] in '@#*':
        now += 1
    else:
        if now > maxi:
            maxi = max(maxi, now)
            rr = i
            ee = i - now
        now = 0
print(maxi)
print(s[ee:rr])