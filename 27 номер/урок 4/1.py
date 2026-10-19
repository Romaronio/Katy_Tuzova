from math import *
from turtle import *
f = open('27_1.txt').readlines()
mas = []
for s in f:
    s = s.split()
    mas.append(s)
point = []
for s in mas:
    one_point = []
    for n in s[:-1]:
        n = float(n)
        one_point.append(n)
    point.append([(1 / 2) * float(s[4]) * (float(s[2]) ** 2 + float(s[3]) ** 2)] + one_point + [s[-1]])

point.sort()
clasters = []
while point:
    clasters.append([point.pop()])
    E1 = clasters[-1][0][0]
    for p1 in clasters[-1]:
        for p2 in point[:]:
            E2 = 1 / 2 * p2[5] * (p2[3] ** 2 + p2[4] ** 2)
            if abs(E1 - E2) < 2:
                clasters[-1].append(p2)
                point.remove(p2)
print(len(clasters))
# k = 20
# pu()
# tracer(0)
# screensize(5000, 5000)
# mas_color = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'brown', 'cyan']
#
# # Проверка количества кластеров
# print(f"Количество кластеров: {len(clasters)}")
#
# for i in range(len(clasters)):
#     if len(clasters[i]) == 0:
#         continue  # Пропускаем пустые кластеры
#     color = mas_color[i % len(mas_color)]  # Защита от выхода за границы списка
#     for p in clasters[i]:
#         goto(p[1] * k, p[2] * k)
#         dot(5, color)  # Увеличили размер для наглядности
# done()
# anti_best_centroid = [[], [], [], []]
# for i in range(len(clasters)):
#     max_sum_dist = 0
#     for E1, x1, y1, V1_1, V2_1, m1, T1 in clasters[i]:
#         max_dist = 0
#         for E2, x2, y2, V1_2, V2_2, m2, T2 in clasters[i]:
#             if T1 == 'II' and T2 == 'II':
#                 max_dist = max(max_dist, dist([x1, y1], [x2, y2]))
#         if max_dist > max_sum_dist:
#             max_sum_dist = max_dist
#             anti_best_centroid[i] = [max_sum_dist]
# print(anti_best_centroid)
# print(int(anti_best_centroid[0][0] * 10_000))

Q1 = 0
for c in clasters:
    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            if c[i][6] == 'II' and c[j][6] == 'II':
                Q1 = max(Q1, dist((c[i][1], c[i][2]), (c[j][1], c[j][2])))
print("Q1 =", int(Q1 * 10000))

best_centroid = []
for i in range(len(clasters)):
    min_sum_dist = float('inf')
    best_E = 0
    for E1, x1, y1, V1_1, V2_1, m1, T1 in clasters[i]:
        sum_dist = 0
        for E2, x2, y2, V1_2, V2_2, m2, T2 in clasters[i]:
            sum_dist += abs(E1 - E2)
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_E = E1
    best_centroid.append(best_E)

print("Энергии центров:", best_centroid)
print("Q2 =", int(max(best_centroid) * 10_000))