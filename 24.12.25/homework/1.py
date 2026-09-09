for n in range(1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '100' + r[3:] + '0'
    else:
        r = '111' + r[3:] + '1'
    if int(r,2) > 128:
        print(n)
        break