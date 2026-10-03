# from math import dist
# f = open('27_A_1.txt')
# mas_point = [list(map(float, s.replace(',', '.').split())) for s in f]
# clsters = [[], []]
# for x, y in mas_point:
#     if y > 10:
#         clsters[0].append([x, y])
#     else:
#         clsters[1].append([x, y])
#
# best_centroid = [[], []]
# for i in range(2):
#     min_dist = 10**8
#     for x1, y1 in clsters[i]:
#         sum_dist = 0
#         for x2, y2 in clsters[i]:
#             sum_dist += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#             # sum_dist = dist([x1, y1], [x2, y2])
#         if min_dist > sum_dist:
#             min_dist = sum_dist
#             best_centroid[i] = [x1, y1]
#
# print(best_centroid)
# P_x_1 = int((sum([x for x, y in best_centroid]) / 2) * 10_000)
# P_y_1 = int((sum([y for x, y in best_centroid]) / 2) * 10_000)
# print(P_x_1, P_y_1)



# from math import dist
# f = open('27_B_1.txt')
# mas_point = [list(map(float, s.replace(',', '.').split())) for s in f]
# clsters = [[], [], []]
# for x, y in mas_point:
#     if y > 12:
#         clsters[0].append([x, y])
#     if x < 5:
#         clsters[1].append([x, y])
#     if y < 0 and x > 20:
#         clsters[2].append([x, y])
#
# best_centroid = [[], [], []]
# for i in range(3):
#     min_dist = 10**8
#     for x1, y1 in clsters[i]:
#         sum_dist = 0
#         for x2, y2 in clsters[i]:
#             sum_dist += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#             # sum_dist = dist([x1, y1], [x2, y2])
#         if min_dist > sum_dist:
#             min_dist = sum_dist
#             best_centroid[i] = [x1, y1]
#
# print(best_centroid)
# P_x_1 = int((sum([x for x, y in best_centroid]) / 3) * 10_000)
# P_y_1 = int((sum([y for x, y in best_centroid]) / 3) * 10_000)
# print(P_x_1, P_y_1)












# mas = [1, 3, 32, 3, 3]
# mas = [list(map(str, mas))]
# print(mas)
# mas1 =  []
# for i in mas:
#     i = str(i)
#     mas1.append(int(i))