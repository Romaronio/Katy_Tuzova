from math import dist
f = open('27_A_1.txt')
mas_point = [list(map(float, s.replace(',', '.').split())) for s in f]
clasters = [[], []]
for x, y in mas_point:
    if y > 10:
        clasters[0].append([x, y])
    else:
        clasters[1].append([x, y])
best_centroid = [[], []]
for i in range(2):
    min_sum_dist = 100000000
    for x1, y1 in clasters[i]:
        sum_dist = 0
        for x2, y2 in clasters[i]:
            sum_dist += dist([x1, y1], [x2, y2])
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroid[i] = [x1, y1]

P_x_1 = int((sum([x for x, y in best_centroid]) / 2) * 10_000)
P_y_1 = int((sum([y for x, y in best_centroid]) / 2) * 10_000)

print(int(P_x_1), int(P_y_1))
#
# from math import dist
# f = open('27_B_1.txt')
# mas_point = [list(map(float, s.replace(',', '.').split())) for s in f]
# clasters = [[], [], []]
# for x, y in mas_point:
#     if x < 5:
#         clasters[0].append([x, y])
#     if y > 10:
#         clasters[1].append([x, y])
#     if y < 0 and x > 10:
#         clasters[2].append([x, y])
# best_centroid = [[], [], []]
# for i in range(3):
#     min_sum_dist = 100000000
#     for x1, y1 in clasters[i]:
#         sum_dist = 0
#         for x2, y2 in clasters[i]:
#             sum_dist += dist([x1, y1], [x2, y2])
#         if sum_dist < min_sum_dist:
#             min_sum_dist = sum_dist
#             best_centroid[i] = [x1, y1]
#
# P_x_1 = int((sum([x for x, y in best_centroid]) / 3) * 10_000)
# P_y_1 = int((sum([y for x, y in best_centroid]) / 3) * 10_000)
#
# print(int(P_x_1), int(P_y_1))



