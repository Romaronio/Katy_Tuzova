s = open('24_2_класс3.txt').readline()
k = 0
n = 0
l = 0
maxi = 0
for r in range(len(s) - 3):
    if s[r] == 'Y':
        k += 1
    if s[r] + s[r + 1] + s[r + 2] + s[r + 3] == '2025':
        n += 1
    while k > 80:
        if s[l] == 'Y':
            k -= 1
        l += 1
    if n >= 90:
        maxi = max(maxi, r - l + 1)
print(maxi)

