#正确的列表推导
board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'
print(board)

#错误示例，包含三个指向同一个列表的引用
weird_board = [['_'] * 3] * 3
#更改其中的一个元素，但实际更改了3个元素
weird_board[1][2] = 'O'
print(weird_board)

#列表的排序
fruits = ['grape', 'raspberry', 'apple', 'banana']
a = sorted(fruits)
b = sorted(fruits, reverse=True)
print(a)
print(b)
#按单词长度排序
c = sorted(fruits, key=len)
print(c)
#就地排序,返回值为None
print(fruits)
d = fruits.sort()
print(d)
print(fruits)
