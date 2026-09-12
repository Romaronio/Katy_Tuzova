# s = 'aaaaabbaaaabbcc' #использовать replace
# c = s.split('b')
# print(c)
# print(max(c))
# print(max(c, key=len))
# print(len(max(c)))
# print(len(max(c, key=len)))


# s = 'aaaaabbaaaabbcc'
# maxlen = 0
# nowlen = 0
# for i in range(len(s)):
#     if s[i] == 'a':
#         nowlen += 1
#     if nowlen > maxlen:
#         maxlen = nowlen
#     else:
#         nowlen = 0
# print(maxlen)

# s = 'aaaaaaaabaaaaaaaabaaaaaabaaaaaabaaaaa'
# k = 0
# l = 0
# m = 0
# for r in range(len(s)):
#     if s[r] == 'b':
#         k += 1
#     while k > 2:
#         if s[l] == 'b':
#             k -= 1
#         l += 1
#     m = max(m, r-l+1)
# print(m)



