s = open('24_4_дз2.txt').readline()
z = 0
l = 0
mini = 100000
for r in range(len(s)):
    if s[r] == 'Z':
        z += 1
    while z > 270 or s[l] != 'Z':
        if s[l] == 'Z':
            z -= 1
        l += 1
    if s[r] == 'Z' and z == 270 and r - l + 1 < mini:
        mini = r - l + 1
print(mini)