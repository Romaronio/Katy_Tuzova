# from re import *
# s = open('24_7_итоговый_тест.txt').readline()
# mass = []
# num = r'((2)([A-Z]|[0-9])(0)([A-Z]|[0-9])(2)([A-Z]|[0-9])(6))'
# reg = rf'(([A-Z]|[0-9])*({num}([A-Z]|[0-9])*){10})'
# for i in finditer(reg, s):
#     t = i.group()
#     mass.append(t)
# print(len(max(mass, key=len)))

s = open('24_7_итоговый_тест.txt').readline()
n = 0
maxi = 0
l = 0
for r in range(len(s)):
    if s[r - 6] + s[r - 4] + s[r - 2] + s[r] == '2026':
        n += 1
    while n > 10:
        if s[l] + s[l + 2] + s[l + 4] + s[l + 6] == '2026':
            n -= 1
        l += 1
    if r - l + 1 > maxi:
        maxi = r - l + 1
print(maxi)