from math import *
from turtle import *
k = 10
tracer(0)
pu()
f = open('27_B_1.txt')
clusters = []
point = [list(map(float, s.split())) for s in f]
print(len(point))
for x, y in point:
    goto(x * k, y * k)
    dot(3, 'blue')
print(len(point))
while point:
    clusters.append([point.pop()])
    for p1 in clusters[-1]:
        for p2 in point[:]:
            if dist(p1, p2) < 1:
                clusters[-1].append(p2)
                point.remove(p2)

print(len(clusters[0]) + len(clusters[1]) + len(clusters[2]))

for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3, 'red')
done()