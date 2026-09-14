s = open('24.7.дз.txt').readline()
s = s.replace('AB', '*')
s = s.replace('AC', '*')
n = 0
maxi = 0
for i in s:
    if i == '*':
        n += 1
    else:
        n = 0
    if n > maxi:
        maxi = n
print(maxi)