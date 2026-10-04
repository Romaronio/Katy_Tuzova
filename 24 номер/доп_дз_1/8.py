s = open('24_доп_дз_8.txt').readline()
s = s.replace('+','*')
s = s.replace('**','@')
n = 0
nn = 0
l = 0
maxi = 0
for r in range(len(s)):
    if s[r] == '*':
        n += 1
    if s[r] == '@':
        nn += 1
    while n > 39 or nn > 0:
        if s[l] == '*':
            n -= 1
        if s[l] == '@':
            nn -= 1
        l += 1
    if n == 39 and nn == 0 and r - l + 1 > maxi and s[r] in '0123456789' and s[l] in '0123456789':
        maxi = r - l + 1
print(maxi)