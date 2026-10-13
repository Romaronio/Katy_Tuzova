s = open('24_2_итоговый_тест.txt').readline()
n = 0
maxi = 0
for i in s:
    if i in 'LISENOK':
        n = 0
    else:
        n += 1
    if n > maxi:
        maxi = n
print(maxi)

# s = open('24_2_итоговый_тест.txt').readline()
# for i in 'LISENOK':
#     s = s.replace(i, '*')
# s = s.split('*')
# print(len(max(s, key=len)))