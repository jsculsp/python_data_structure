from BSTMap import BSTMap
from AVLMap import AVLMap
from random import randrange
import time

b = BSTMap()
a = AVLMap()

time_start = time.clock()
for i in range(10 ** 5):
	b.add(randrange(10 ** 6))
time_end = time.clock()
time1 = time_end - time_start

time_start = time.clock()
for i in range(10 ** 5):
	a.add(randrange(10 ** 6))
time_end = time.clock()
time2 = time_end - time_start

print('BSTMap runs for %s seconds...' % time1)
print('AVLMap runs for %s seconds...' % time2)


