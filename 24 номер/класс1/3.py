# f = open('24.4.класс.txt')
# s = f.readline()
# for i in s:
#     if i not in '0123456789AB':
#         s = s.replace(i, '#')
# s = s.split('#')
# print(max(s))

f = open('24.4.класс.txt')
s = f.readline()
n = 0
maxn = 0
for i in s:
    if i in '0123456789AB':
        n += 1
    else:
        n = 0
    if n > maxn:
        maxn = n
print(maxn)
