s = open('24_7_дз4.txt').readline()
s = s.replace('+', '*')
n = 0
maxi = 0
for i in range(len(s) - 1):
    if s[i] + s[i + 1] == '**':
        if n != 0 and n + 1 > maxi:
            maxi = n + 1
        n = 0
    else:
        n += 1
print(maxi)