s = open('24.2.дз.txt').readline()
for i in s:
    if i in '02468':
        s = s.replace(i, '*')
    elif i in '13579':
        s = s.replace(i, '#')
s = s.replace('*#', '@')
s = s.split('@')
print(len(max(s, key=len)))
#смотри в чем ошибка, у тебя не должно быть рядом стоящих четных и нечетных числе,
# а у тебя получилось что нет рядом стоящих одинаковых чисел