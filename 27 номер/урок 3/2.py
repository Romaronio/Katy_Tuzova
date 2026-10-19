# from math import *
# from turtle import *
# f = open('27_A_2.txt').readlines()
# point = [list(map(float, s.replace(',', '.').split())) for s in f]
# # k = 20
# # screensize(5000, 5000)
# # pu()
# # tracer(0)
# # for x in range(-20, 20):
# #     for y in range(-20, 20):
# #         goto(x * k, y * k)
# #         dot(3, 'blue')
#
# clasters = []
# while point:
#     clasters.append([point.pop()])
#     for p1 in clasters[-1]:
#         for p2 in point[:]:
#             if dist(p1, p2) < 0.5:
#                 clasters[-1].append(p2)
#                 point.remove(p2)
#
# best_centroid = [[], []]
# for i in range(2):
#     max_sum_dist = -1
#     for x1, y1 in clasters[i]:
#         sum_dist = 0
#         for x2, y2 in clasters[i]:
#             sum_dist += dist((x1, y1), (x2, y2))
#         if sum_dist > max_sum_dist:
#             max_sum_dist = sum_dist
#             best_centroid[i] = [x1, y1]
# print(best_centroid)
# print(int((best_centroid[1][0] + best_centroid[1][1])* 10_000))
# print(int((best_centroid[0][0] + best_centroid[0][1])* 10_000))



from math import *
from turtle import *
f = open('27_B_2.txt').readlines()
point = [list(map(float, s.replace(',', '.').split())) for s in f]
clasters = []
while point:
    clasters.append([point.pop()])
    for p1 in clasters[-1]:
        for p2 in point[:]:
            if dist(p1, p2) < 1:
                clasters[-1].append(p2)
                point.remove(p2)

clasters = [c for c in clasters if len(c) > 1]


best_centroid = [[], [], []]
for i in range(3):
    max_sum_dist = -1
    for x1, y1 in clasters[i]:
        sum_dist = 0
        for x2, y2 in clasters[i]:
            sum_dist += dist((x1, y1), (x2, y2))
        if sum_dist > max_sum_dist:
            max_sum_dist = sum_dist
            best_centroid[i] = [x1, y1]

anti_centroid1 = dist(best_centroid[0], (0, 0))
anti_centroid2 = dist(best_centroid[1], (0, 0))
anti_centroid3 = dist(best_centroid[2], (0, 0))
print(anti_centroid1, anti_centroid2, anti_centroid3)
Q_x = int(best_centroid[2][0] * 10_000)
Q_y = int(best_centroid[1][1] * 10_000)
print(Q_x, Q_y)
done()