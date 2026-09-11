# f = open('24.7.класс.txt')
# s = f.readline()
# for i in s:
#     if i in '13579':
#         s = s.replace(i,'*')
# s = s.split('*')
# print(max(s))

f = open('24.7.класс.txt')
s = f.readline()
n = 0
maxn = 0
s = s.replace('1','*')
s = s.replace('3','*')
s = s.replace('5','*')
s = s.replace('7','*')
s = s.replace('9','*')
s = s.split('***')
print(len(max(s, key=len)))
# for i in s:
#     if i != ('*'):
#         n += 1
#     else:
#         n = 0
#     if n > maxn:
#         maxn = n
# print(maxn)