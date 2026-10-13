s = open('24_доп_дз_2.txt').readline()
f = 0
l = 0
maxi = 0
for r in range(len(s)):
    if s[r] == 'F':
        f += 1
    while f > 1:
        if s[l] == 'F':
            f -= 1
        l += 1
    if f == 1 and r - l + 1 > maxi:
        maxi = r - l + 1
print(maxi)