for n in range(1000):
    r = bin(n)[2:]
    s = ''
    for i in r[1:-1]:
        if i == '1':
            s += '0'
        else:
            s += '1'
    s = r[0] + s + r[-1]
    a = int(s, 2) + n
    if n % 2 == 1 and a > 300:
        print(n)
        break