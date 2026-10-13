s = open('24.2.дз.txt').readline()
n = 0
l = 0
maxi = 0
for i in s:
    if i in '02468':
        s = s.replace(i, '*')
    elif i in '13579':
        s = s.replace(i, '#')
for i in range(len(s)):
    if s[i - 1] + s[i] == '*#' or s[i - 1] + s[i] == '#*':
        n += 1
    while n > 0:
        if s[l] + s[l + 1] == '*#' or s[l] + s[l + 1] == '#*':
            n -= 1
        l += 1
    if i - l + 1 > maxi:
        maxi = i - l + 1
print(maxi)
#смотри в чем ошибка, у тебя не должно быть рядом стоящих четных и нечетных числе,
# а у тебя получилось что нет рядом стоящих одинаковых чисел