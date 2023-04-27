fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
a = sorted(fruits, key=len)
print(a)

def reverse(word):
    return word[::-1]

b = reverse('testing')
print(b)

c = sorted(fruits, key=reverse)
print(c)

