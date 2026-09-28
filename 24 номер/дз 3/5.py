s = open('24_5_дз3.txt').readline()
s = s.replace('1', '#')
s = s.replace('2', '*')
s = s.replace('3', '#')
s = s.replace('4', '*')
s = s.replace('5', '#')
s = s.replace('*#','@')
n = 0
maxi = 0
for i in s:
    if i == '@':
        n += 1
    else:
        n = 0
    if n > maxi:
        maxi = n
print(maxi)