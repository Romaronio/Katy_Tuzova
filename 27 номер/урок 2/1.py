# from math import dist
# f = open('27_A_1.txt')
# point = []
# for s in f:
#     s = s.replace(',', '.').split()
#     x, y, z = s
#     x, y = float(x), float(y)
#     point.append([x, y, z])
#
# clasters = [[], []]
# for x, y, z in point:
#     if y > 10:
#         clasters[0].append([x, y, z])
#     else:
#         clasters[1].append([x, y, z])
#
# print(len(clasters[0]), len(clasters[1]))
#
# best_centroid = [[], []]
# for i in range(len(clasters)):
#     min_sum_dist = 10 ** 8
#     for x1, y1, z1 in clasters[i]:
#         sum_dist = 0
#         for x2, y2, z2 in clasters[i]:
#             sum_dist += dist((x1, y1), (x2, y2))
#         if sum_dist < min_sum_dist:
#             min_sum_dist = sum_dist
#             best_centroid[i] = [x1, y1, z1]
# print(best_centroid)
#
# red_giant = []
# for x, y, z in point:
#     a, b, c = z[0], z[1], z[2:]
#     if c == 'III' and a == 'Y':
#         red_giant.append([x, y, z])
#
# print(len(red_giant))
# print(red_giant)
#
#
# min_sum_dist = []
# for x, y, z in red_giant:
#     x1, y1, z1 = best_centroid[0][0], best_centroid[0][1], best_centroid[0][2]
#     min_sum_dist.append(dist((x, y), (x1, y1)))
# print(int(min(min_sum_dist) * 10_000))
# print(int(max(min_sum_dist) * 10_000))

from math import dist
f = open('27_B_1.txt')
point = []
for s in f:
    s = s.replace(',', '.').split()
    x, y, z = s
    x, y = float(x), float(y)
    point.append([x, y, z])

clasters = [[], [], []]
for x, y, z in point:
    if y < 16:
        clasters[0].append([x, y, z])
    if y > 22:
        clasters[1].append([x, y, z])
    else:
        clasters[2].append([x, y, z])

print(len(clasters[0]), len(clasters[1]), len(clasters[2]))

best_centroid = [[], [], []]
for i in range(len(clasters)):
    min_sum_dist = 10 ** 8
    for x1, y1, z1 in clasters[i]:
        sum_dist = 0
        for x2, y2, z2 in clasters[i]:
            sum_dist += dist((x1, y1), (x2, y2))
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroid[i] = [x1, y1, z1]
print(best_centroid)

yellow_super_giant = [[], [], []]
for i in range(3):
    for x, y, z in clasters[i]:
        a, b, c = z[0], z[1], z[2:]
        if c == 'I' and a == 'Z':
            yellow_super_giant[i].append([x, y, z])

print(len(yellow_super_giant[0]), len(yellow_super_giant[1]), len(yellow_super_giant[2]))
print(yellow_super_giant)


# min_sum_dist = []
# for x, y, z in red_giant:
#     x1, y1, z1 = best_centroid[0][0], best_centroid[0][1], best_centroid[0][2]
#     min_sum_dist.append(dist((x, y), (x1, y1)))
# print(int(min(min_sum_dist) * 10_000))
# print(int(max(min_sum_dist) * 10_000))

