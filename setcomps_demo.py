from unicodedata import name


#集合推导
a = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}
print(a)

#如果用 b = {} 进行构造，那么构造出来的是字典
b = set()
print(type(b))


c = {1, 2, 3}
print(type(c))