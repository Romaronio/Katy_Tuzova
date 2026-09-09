for n in range(1000):
    r = bin(n)[2:]
    if n % 5 == 0:
        r += '11'
    else:
        r += bin(n//5)[2:]
    if int(r,2) > 896 and n % 2 == 0:
        print(n)
        break