s = open('24_3_класс3.txt').readline()
k = 0
n = 0
l = 0
maxi = 0
ll = 0
rr = 0
for r in range(len(s)):
    if s[r] == k and s[r] in 'AEIOUY':
        maxi = max(maxi, r - l + 1)
        ll = l
        rr = r
    if s[r] not in '0123456789':
        k = s[r]
        l = r
print(maxi)
print(s[ll:rr + 1])