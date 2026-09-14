s = open('24_1__класс3.txt').readline()
k = 0
ch = 0
l = 0
maxi = 0
ll = 0
rr = 0
for r in range (len(s)):
    if s[r] == 'S':
        k += 1
    if s[r] in '24680':
        ch += 1
    while k > 35 or ch > 1 or s[l] not in '24680':
        if s[l] == 'S':
            k -= 1
        if s[l] in '24680':
            ch -= 1
        l += 1
    if k == 35:
        maxi = max(maxi, r - l + 1)
        ll = l
        rr = r
print(s[ll:rr + 1])
print(s[ll:rr + 1].count('0'))
print(s[ll:rr + 1].count('2'))
print(s[ll:rr + 1].count('4'))
print(s[ll:rr + 1].count('6'))
print(s[ll:rr + 1].count('8'))
print(s[ll:rr + 1].count('S'))
print(maxi)
