s = open('24_доп_дз_5.txt').readline()
dd = 0
fe = 0
l = 0
maxi = 0
for r in range(len(s)):
    if s[r - 1] + s[r] == 'DD':
        dd += 1
    elif s[r - 1] + s[r] == 'FE':
        fe += 1
    while dd > 0:
        if s[l] + s[l + 1] == 'DD':
            dd -= 1
        if s[l] + s[l + 1] == 'FE':
            fe -= 1
        l += 1
    if dd == 0 and fe >= 1 and r - l + 1 > maxi:
        maxi = r - l + 1
print(maxi)