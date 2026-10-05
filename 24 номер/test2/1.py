s = open('24_1.txt').readline()
n = 0
maxi = 0
sim = 0
for i in s:
    if int(i) >= sim:
        n += 1
        sim = int(i)
    else:
        n = 1
        sim = int(i)
    if n > maxi:
        maxi = n
print(maxi)

from re import*
s2 = open('24_1.txt').readline()
mass = []
reg = r'([0]*[1]*[2]*[3]*[4]*[5]*[6]*[7]*[8]*[9]*)'
for i in finditer(reg, s2):
    t = i.group()
    mass.append(t)
print(len(max(mass, key=len)))