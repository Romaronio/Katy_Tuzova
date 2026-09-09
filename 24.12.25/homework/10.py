def seven(n):
    s = ''
    while n:
        s = str(n % 7) + s
        n //= 7
    return s
max = 0
for n in range(1,1000):
    r = seven(n)
    if r[-1] == '2':
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
        a = '1' + r[1:] + '36'
    if int(a,7) < 744 and int(a,7) > max:
        max = int(a,7)
        N = n
print(N)