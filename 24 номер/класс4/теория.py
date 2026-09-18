# from re import *
# s = 'просто какая то строка провто предложение про'
# reg = '(про)+[а-я]*'
# for i in finditer(reg, s):
#     print(i.group())


# from re import *
# s = '213+23213+2134213+213+214+214'
# reg = '(213)|(214)'
# for i in finditer(reg, s):
#     print(i.group())

# from re import *
# s = open('24_0_класс4.txt').readline()
# reg = '[B]+'
# mas = []
# for i in finditer(reg, s):
#     t = i.group()
#     print(t)
#     mas.append(t)
# print(len(max(mas, key=len)))


# from re import *
# s = open('24.2.класс.txt').readline()
# reg = '((ZXY)|(ZYX))+'
# mas = []
# for i in finditer(reg, s):
#     i = i.group()
#     print(i)
#     mas.append(i)
# print(len(max(mas, key=len)))


# from re import *
# s = open('24_3_класс4.txt').readline()
# reg = '([BC][BC](A))*'
# mas = []
# for i in finditer(reg, s):
#     i = i.group()
#     mas.append(i)
# print(len(max(mas, key=len)))
# print(max(mas, key=len))


# from re import *
# s = open('24_4_класс4.txt').readline()
# reg = '([1-9]|[AB])+'
# mas = []
# for i in finditer(reg, s):
#     mas.append(i.group())
# print(len(max(mas, key=len)))


# from re import *
# s = open('24_5_класс4.txt').readline()
# # s = s.replace('*', 'A').replace('+', 'B')
# num = '([1-9][0-9]*[24680])+'
# reg = f'({num}([*+]{num}|0)*)+'
# mas = []
# for i in finditer(reg, s):
#     i = i.group()
#     print(i)
#     mas.append(i)
# print(len(max(mas, key=len)))
# print(max(mas, key=len))


# from re import *
# s = 'abaaaaabaaaaaabaaaaaaabaaaa'
# reg = '(?=([a]*[b][a]*[b][a]*))'
# mas = []
# for i in finditer(reg, s):
#     i = i.group(1)
#     mas.append(i)
# print(len(max(mas, key=len)))


