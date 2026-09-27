s = open('24.8.дз.txt').readline()
pr = 0
st = 0
n = 0
maxi = 0
for i in range(len(s) - 1):
    if pr == 0 or st == 0:
        if s[i] + s[i + 1]  == 'PR':
            pr += 1
            n += 1
        elif s[i] + s[i + 1] == 'ST':
            st += 1
            n += 1
        else:
            n += 1
        if n > maxi:
            maxi = n
    else:
        n = 0
        pr = 0
        st = 0
print(maxi)#не учла тот факт, что строка может начниать на r, вметсто pr и на t вместо st
#аналогично с концом, строка может заканчиваться на p и на s