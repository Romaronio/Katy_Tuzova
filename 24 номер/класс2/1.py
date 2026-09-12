s = open('24.1.класс2.txt').readline()
l = 0
k = 0
m = 0
# s = 'bdbcbcbcbcbcbcbcbdsdfsdfbdcbscbbc'
for r in range(len(s)-1):
    if s[r] + s[r + 1] == 'BC':
        k += 1
    while k > 190:
        if s[l] + s[l + 1] == 'BC':
            k -= 1
        l += 1
    m = max(m, r-l+2)
print(m)
