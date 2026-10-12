# f = open('27_A_1.txt').readlines()
# mas_point = []
# for s in f:
#     mas_point.append(s.split())
# for i in range(len(mas_point)):
#     mas_point[i][0] = float(mas_point[i][0].replace(',','.'))
#     mas_point[i][1] = float(mas_point[i][1].replace(',', '.'))

# from math import dist
# f = open('27_A_1.txt')
# point = []
# for s in f:
#     s = s.replace(',', '.').split()
#     x, y, z = s
#     x, y = float(x), float(y)
#     point.append([x, y, z])
# print(point)
#
# claster = [[], []]
# for x, y, z in point:
#     if y > 10:
#         claster[0].append([x, y, z])
#     else:
#         claster[1].append([x, y, z])
#
# best_centroid = [[], []]
# for i in range(2):
#     min_sum_dist = 10 ** 8
#     for x1, y1, z1 in claster[i]:
#         sum_dist = 0
#         for x2, y2, z2 in claster[i]:
#             sum_dist += dist((x1, y1), (x2, y2))
#         if sum_dist < min_sum_dist:
#             min_sum_dist = sum_dist
#             best_centroid[i] = [x1, y1, z1]
#
# print(best_centroid)
#
# mas_red = []
# for x, y, z in point:
#     if z[0] + z[2:] == 'YIII':
#         mas_red.append([x, y, z])
# print(mas_red)
#
# mas_red_gigant_dist = []
# for x, y, z in mas_red:
#     mas_red_gigant_dist.append(dist((x, y), (best_centroid[0][0], best_centroid[0][1])))
# print(int(min(mas_red_gigant_dist) * 10_000))
# print(int(max(mas_red_gigant_dist) * 10_000))


from math import dist
f = open('27_B_1.txt')
point = []
for s in f:
    s = s.replace(',', '.').split()
    x, y, z = s
    x, y = float(x), float(y)
    point.append([x, y, z])

claster = [[], [], []]
for x, y, z in point:
    if y > 23:
        claster[0].append([x, y, z])
    elif y < 16:
        claster[1].append([x, y, z])
    else:
        claster[2].append([x, y, z])

best_centroid = [[], [], []]
for i in range(3):
    min_sum_dist = 10 ** 8
    for x1, y1, z1 in claster[i]:
        sum_dist = 0
        for x2, y2, z2 in claster[i]:
            sum_dist += dist((x1, y1), (x2, y2))
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroid[i] = [x1, y1, z1]

print(best_centroid)

yellow_super_gigamt = [[], [], []]
for i in range(3):
    for x1, y1, z1 in claster[i]:
        if z1[0] == 'Z' and z1[2:] == 'I':
            yellow_super_gigamt[i].append([x1, y1, z1])
print(len(yellow_super_gigamt[0]), len(yellow_super_gigamt[1]), len(yellow_super_gigamt[2]))
print(int(dist((best_centroid[2][0], best_centroid[2][1]), (best_centroid[1][0], best_centroid[1][1])) * 10_000))
# yellow_super_gigamt = [[], [], []]
# for i in range(3):
#     min_sum_dist = 10 ** 8
#     for x1, y1, z1 in claster[i]:
#         for x2, y2, z2 in claster[i]:
#             if z1[0] == 'Z' and z1[2:] == 'I' and z2[0] == 'Z' and z2[2:] == 'I' and x1 != x2 and y1 != y2 and z1 != z2:
#                 if dist((x1, y1), (x2, y2)) < min_sum_dist:
#                     min_sum_dist = dist((x1, y1), (x2, y2))
#                     yellow_super_gigamt[i] = min_sum_dist
# print(yellow_super_gigamt)
# print(int(min(yellow_super_gigamt) * 10_000))









