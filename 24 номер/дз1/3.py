s = open('24.3.дз.txt').readline()
n = 0
maxi = 0
for i in s:
    if i in '0123456789AB':
        n += 1
    else:
        n = 0
    if n > maxi:
        maxi = n
print(maxi)