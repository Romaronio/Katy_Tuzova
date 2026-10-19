# from turtle import *
# from math import *
# f = open('27_1.txt').readlines()
# def E(m, Vx, Vy):
#     return 0.5 * m * (Vx ** 2 + Vy ** 2)
# point = []
# for line in f:
#     line = line.split()
#     for i in range(len(line[:-1])):
#         line[i] = float(line[i])
#     line = [E(line[4], line[2], line[3])] + line
#     point.append(line)
#
#
#
# point.sort()
# clasters = []
# while point:
#     clasters.append([point.pop()])
#     for E1, x1, y1, Vx1, Vy1, m1, p1 in point[:]:
#         if abs(clasters[-1][0][0] - E1) < 2:
#             clasters[-1].append([E1, x1, y1, Vx1, Vy1, m1, p1])
#             point.remove([E1, x1, y1, Vx1, Vy1, m1, p1])
#
# # tracer(0)
# # screensize(5000, 5000)
# # k = 10
# # pu()
# # for x in range(-40, 40):
# #     for y in range(-40, 40):
# #         goto(x * k, y * k)
# #         dot(3)
# # mas = ['red', 'blue', 'green', 'yellow']
# # for i in range(len(clasters)):
# #     for E, x, y, Vx, Vy, m, p in clasters[i]:
# #         goto(x * k, y * k)
# #         dot(4, mas[i])
# # done()
#
# Best_q = []
# for i in range(len(clasters)):
#     max_dist = 0
#     for E1, x1, y1, Vx1, Vy1, m1, p1 in clasters[i]:
#         for E2, x2, y2, Vx2, Vy2, m2, p2 in clasters[i]:
#             if p1 == 'II' and p2 == 'II' and max_dist < dist([x1, y1], [x2, y2]):
#                 max_dist = dist([x1, y1], [x2, y2])
#     Best_q.append(max_dist)
# print(int(max(Best_q) * 10_000))
# # 539936 100704
#
# Best_centroid = [[], [], [], []]
# for i in range(len(clasters)):
#     min_E = 10 ** 8
#     for E1, x1, y1, Vx1, Vy1, m1, p1 in clasters[i]:
#         sum_modul_E = 0
#         for E2, x2, y2, Vx2, Vy2, m2, p2 in clasters[i]:
#             sum_modul_E = sum_modul_E + abs(E1 - E2)
#         if sum_modul_E < min_E:
#             min_E = sum_modul_E
#             Best_centroid[i] = [E1]
# print(int(Best_centroid[0][0] * 10_000))


# cl = [[],[],[],[]]
# for s in open('27_1.txt'):
#     x,y,vx,vy,m,t = s.replace(',','.').split()
#     x,y,vx,vy,m = map(float,[x,y,vx,vy,m])
#     E = 0.5*m*(vx**2+vy**2)
#     if E<3.5: cl[0].append([x,y,E,t])
#     elif E<6: cl[1].append([x,y,E,t])
#     elif E<8.5: cl[2].append([x,y,E,t])
#     else: cl[3].append([x,y,E,t])
# def dist(p1,p2):
#     x1,y1,e1,t1 = p1
#     x2,y2,e2,t2 = p2
#     return ((x2-x1)**2 + (y2-y1)**2)**0.5
# def centr(cl):
#     m = []
#     for p in cl:
#         s = sum(abs(p[2]-p1[2]) for p1 in cl)
#         m.append([s,p])
#     return min(m)[1][2]
# q1 = max([dist(p,p1) for p in cl[0] for p1 in cl[0] if p[3]=='II' and p1[3]=='II']+\
#          [dist(p,p1) for p in cl[1] for p1 in cl[1] if p[3]=='II' and p1[3]=='II']+\
#          [dist(p,p1) for p in cl[2] for p1 in cl[2] if p[3]=='II' and p1[3]=='II']+\
#          [dist(p,p1) for p in cl[3] for p1 in cl[3] if p[3]=='II' and p1[3]=='II'])
# q2 = max([centr(k) for k in cl])
# print(int(q1*10000), int(q2*10000))