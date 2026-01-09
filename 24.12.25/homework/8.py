def three(n):
    s = ''
    while n:
        s = str(n % 3) + s
        n //= 3
    return s
for n in range(1000):
    r = three(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + three((n % 3) * 4)
    if int(r,3) < 100:
        max = n
print(max)