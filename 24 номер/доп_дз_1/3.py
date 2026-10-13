s = open('24_доп_дз_3.txt').readline()
for i in 'ABCD':
    s = s.replace(i, '*')
s = s.split('*')
print(len(max(s, key=len)))