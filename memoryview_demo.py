import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))

memv_oct = memv.cast('B')
a = memv_oct.tolist()
print(a)