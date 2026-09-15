s = open('24.9.дз.txt').readline()
s = s.replace('A', '*')
s = s.replace('C', '#')
s = s.replace('D', '#')
s = s.replace('F', '#')
s = s.replace('O', '*')
s = s.split('#**#')
print(len(max(s, key=len)))
#опять же потеряла балл из за того что забыла что в конце и в начале может стоять какое сочетакние символов из #**#
#очень аккуратно!!!