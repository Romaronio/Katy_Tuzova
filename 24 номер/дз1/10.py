s = open('24.10.дз.txt').readline()
s = s.replace('XYZY', '@')
s = s.replace('Y', '*')
s = s.replace('X', '#')
s = s.replace('Z', '#')
s = s.replace('#*', '!')
n = 0
maxi = 0
for i in s:
    if i == '!':
        n += 1
    else:
        n = 0
    if n > maxi:
        maxi = n
print(maxi)