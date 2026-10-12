f = open('27_A_1_дз_1.txt').readlines()
from turtle import *
point = [list(map(float, s.replace(',', '.').split())) for s in f]


clasters = [[], []]
for x, y in point:
    if y > -x + 10:
        clasters[0].append([x, y])
    else:
        clasters[1].append([x, y])
print(len(point))
print(len(clasters[0]) + len(clasters[1]))

k = 20
tracer(0)
pu()
for x, y in point:
    goto(x * k, y * k)
    dot(3)

for x in range(-40, 40):
     for y in range(-40, 40):
         if y * k == -x * k + 10 * k and y > 0:
             goto(x * k, y * k)
             dot(5, 'blue')
         else:
             goto(x * k, y * k)
             dot(3, 'red')
done()