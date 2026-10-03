# f = open('27_A_2.txt')
# mas_point = [list(map(float, s.split())) for s in f]
#
# clasters = [[], []]
# for x, y in mas_point:
#     if y < 10:
#         clasters[0].append([x, y])
#     else:
#         clasters[1].append([x, y])
#
# best_centroid = [[], []]
# for i in range(2):
#     min_dist = 10**8
#     for x1, y1 in clasters[i]:
#         sum_dist = 0
#         for x2, y2 in clasters[i]:
#             sum_dist += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#         if sum_dist < min_dist:
#             min_dist = sum_dist
#             best_centroid[i] = [x1, y1]
#
# P_x_1 = int((best_centroid[0][0] + best_centroid[1][0]) * 10_000)
# P_y_1 = int((best_centroid[0][1] + best_centroid[1][1]) * 10_000)
#
# # P_x_2 = sum([x for x, y in best_centroid])
# # P_y_2 = sum([y for x, y in best_centroid])
#
# print(P_x_1, P_y_1)


from math import dist
f = open('27_B_2.txt')
mas_point = [list(map(float, s.split())) for s in f]
for x, y in mas_point:
    if x < 7 or x > 30:
        mas_point.remove([x, y])


clasters = [[], [], []]
for x, y in mas_point:
    if y > 21:
        clasters[0].append([x, y])
    if y > 15 and y < 21:
        clasters[1].append([x, y])
    if y < 15:
        clasters[2].append([x, y])

best_centroid = [[], [], []]
for i in range(3):
    min_dist = 10**8
    for x1, y1 in clasters[i]:
        sum_dist = 0
        for x2, y2 in clasters[i]:
            sum_dist += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if sum_dist < min_dist:
            min_dist = sum_dist
            best_centroid[i] = [x1, y1]
print(best_centroid)
#
# Q_1 = int(((best_centroid[1][0] ** 2 + best_centroid[1][1] ** 2) ** 0.5) * 10_000)
# Q_2 = int(((best_centroid[0][0] ** 2 + best_centroid[0][1] ** 2) ** 0.5) * 10_000)
Q_1 = int(max([dist([x1, y1], [0, 0]) for x1, y1 in best_centroid]) * 10_000)
Q_2 = int(min([dist([x1, y1], [0, 0]) for x1, y1 in best_centroid]) * 10_000)
print(Q_1, Q_2)


