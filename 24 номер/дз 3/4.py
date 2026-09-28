s = open('24_4_дз3.txt').readline()
b = 0
ll = 0
l = 0
maxi = 0
for r in range(len(s)):
    if s[r] not in '0123456789':
        b += 1
    while b > 2 or s[l] in '0123456789':
        if s[l] not in '0123456789':
            b -= 1
        l += 1
    if b == 2 and s[r] not in '0123456789' and s[r] == s[l] and r - l + 1 > maxi:
        maxi = r - l + 1
        ll = l
print(ll)