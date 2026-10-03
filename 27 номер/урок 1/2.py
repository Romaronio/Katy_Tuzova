# f = open('27_A_2.txt')
# from math import dist
# mas_point = [list(map(float, s.replace(',', '.').split())) for s in f]
# k = 2
# claster = [[] for i in range(k)]
# for x, y in mas_point:
#     if y > 10:
#         claster[0].append([x, y])
#     else:
#         claster[1].append([x, y])
#
# best_centroid = [[], []]
# for i in range(2):
#     min_sum_dist = 100000000
#     for x1, y1 in claster[i]:
#         sum_dist = 0
#         for x2, y2 in claster[i]:
#             sum_dist += dist([x1, y1], [x2, y2])
#         if sum_dist < min_sum_dist:
#             min_sum_dist = sum_dist
#             best_centroid[i] = [x1, y1]
#
# P_x_1 = int(sum([x for x, y in best_centroid]) * 10_000)
# P_y_1 = int(sum([y for x, y in best_centroid]) * 10_000)
# print(P_x_1, P_y_1)


# f = open('27_B_2.txt')
# from math import dist
# mas_point = [list(map(float, s.replace(',', '.').split())) for s in f]
#
# claster = [[] for i in range(3)]
# for x, y in mas_point:
#     if y > 21 and x < 20 and x > 10:
#         claster[0].append([x, y])
#     if y < 21 and x < 20 and x > 10:
#         claster[1].append([x, y])
#     if x > 20 and x < 30:
#         claster[2].append([x, y])
#
# best_centroid = [[], [], []]
# for i in range(3):
#     min_sum_dist = 100000000
#     for x1, y1 in claster[i]:
#         sum_dist = 0
#         for x2, y2 in claster[i]:
#             sum_dist += dist([x1, y1], [x2, y2])
#         if sum_dist < min_sum_dist:
#             min_sum_dist = sum_dist
#             best_centroid[i] = [x1, y1]
#
# Min_dist = int(min([dist([x1, y1], [0, 0]) for x1, y1 in best_centroid]) * 10_000)
# Max_dist = int(max([dist([x1, y1], [0, 0]) for x1, y1 in best_centroid]) * 10_000)
# print(Min_dist, Max_dist)