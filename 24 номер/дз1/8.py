s = open('24.8.дз.txt').readline()
s = s.replace('PR', '*')
s = s.replace('ST', '#')
pr = 0
st = 0
n = 0
maxi = 0
for i in s:
    if pr == 0 or st == 0:
        if i == '*':
            pr += 1
            n += 2
        elif i == '#':
            st += 1
            n += 2
        else:
            n += 1
    else:
        n = 0
        pr = 0
        st = 0
    if n > maxi:
        maxi = n
print(maxi)#не учла тот факт, что строка может начниать на r, вметсто pr и на t вместо st
#аналогично с концом, строка может заканчиваться на p и на s