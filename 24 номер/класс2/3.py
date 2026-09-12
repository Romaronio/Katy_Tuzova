s = open('24.3.класс2.txt').readline()
l = 0
k = 0
m = 0
for r in range(len(s)):
    if s[r] == 'T':
        k += 1
    while k > 100:
        if s[l] == 'T':
            k -= 1
        l += 1
    m = max(m, r-l+1)
print(m)
