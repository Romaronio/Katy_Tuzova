from math import dist
f = open('27_A_1_дз_1.txt').readlines()
mass = [list(map(float, s.replace(',', '.').split())) for s in f]

clasters = [[], []]
for x, y in mass:
    if y > -x + 10:
        clasters[0].append([x, y])
    else:
        clasters[1].append([x, y])

centers = [[], []]
for i in range(2):
    min_dist = 10 ** 8
    for x1, y1 in clasters[i]:
        sum_dist = 0
        for x2, y2 in clasters[i]:
            sum_dist += dist([x1, y1], [x2, y2])
        if sum_dist < min_dist:
            min_dist = sum_dist
            centers[i] = [x1, y1]

Px = (int((centers[0][0] + centers[1][0]) / 2 * 100))
Py = (int((centers[0][1] + centers[1][1]) / 2 * 100))


f2 = open('27_B_1_дз_1.txt').readlines()
mass2 = [list(map(float, s.replace(',', '.').split())) for s in f2]

clasters2 = [[], [], []]
for x, y in mass2:
    if y > 2 and x < 4:
        clasters2[0].append([x, y])
    elif y > 2 and x > 4:
        clasters2[1].append([x, y])
    else:
        clasters2[2].append([x, y])

centers2 = [[], [], []]
for i in range(3):
    min_dist = 10 ** 8
    sum_dist = 0
    for x1, y1 in clasters2[i]:
        for x2, y2 in clasters2[i]:
            sum_dist += dist([x1, y1], [x2, y2])
        if sum_dist < min_dist:
            min_dist = sum_dist
            centers2[i] = [x1, y1]

Px2 = (int((centers2[0][0] + centers2[1][0] + centers2[2][0]) / 3 * 100))
Py2 = (int((centers2[0][1] + centers2[1][1] + centers2[2][1]) / 3 * 100))

print(Px, Py)
print(Px2, Py2)