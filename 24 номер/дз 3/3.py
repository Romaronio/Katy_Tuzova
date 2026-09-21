s = open('24_3_дз3.txt').readline()
n = 0
l = 0
mini = 100000
for r in range(len(s) - 2):
    if s[r] + s[r + 1] + s[r + 2] == 'ABC':
        n += 1
    while n > 60:
        if s[l] + s[l + 1] + s[l + 2]  == 'ABC':
            n -= 1
        l += 1
    if n == 60 and r - l + 1 < mini and s[r] == 'C':
        mini = r - l + 1
print(mini)