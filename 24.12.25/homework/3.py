max = 0
for n in range(13):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    if int(r,2) > max:
        max = int(r,2)
        N = n
print(max)