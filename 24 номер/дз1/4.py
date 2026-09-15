s = open('24.4.дз.txt').readline()
n = 0
ch = 0
maxi = 0
for i in range(len(s)):
    if ch == 0 and s[i] in '123456789AB': #не правильно прописала условие, чтоб число не начиналось с нуля. попробуй перерделать
        n += 1
        ch += 1
    elif s[i] in '0123456789AB':
        n += 1
    else:
        n = 0
        ch = 0
    if n > maxi and s[i] in '02468A':
        maxi = n
print(maxi)