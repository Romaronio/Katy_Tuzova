def four(n):
    s = ''
    while n:
        s = str(n % 4) + s
        n //= 4
    return s
for n in range(1,1000):
    r = four(n)
    if r[0] == '3':
        a = ''
        for i in r:
            if i == '3':
                a += '1'
            elif i == '1':
                a += '3'
            else:
                a += i
        a = '21' + a
    else:
        a = '1' + r[1:] + '12'
    if int(a,4) < 598:
        max = n
print(max)