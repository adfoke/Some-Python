from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
print(floats[-1] )

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
