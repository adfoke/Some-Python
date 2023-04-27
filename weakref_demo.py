import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
wref()
a_set = {2, 3, 4} 
print(wref() is None)