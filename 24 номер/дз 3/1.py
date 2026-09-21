s = open('24_1_дз3.txt').readline()
maxi = 0
for i in s:
    if i in '0468':
        s = s.replace(i, '2')
s = s.split('2')
for i in s:
    if len(set(i)) == 1:
        if len(i) > maxi:
            maxi = len(i)
print(maxi + 2)