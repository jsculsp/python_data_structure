# Sorts a sequence of positive integers using the radix sort algorithm.

from linklistqueue import Queue
from my_own_array import Array

def radixSort(intList, numDigits):
	# Create an arrry of queues to represent the bins.
	binArray = Array(10)
	for k in range(10):
		binArray[k] = Queue()
		
	# The value of the current column.
	column = 1
	
	# Iterate over the number of digits in the largest value.
	for d in range(numDigits):
		
		# Distribute the keys across the 10 bins.
		for key in intList:
			digit = (key // column) % 10
			binArray[digit].enqueue(key)
			
		# Gather the keys from the bins and place them back in intList.
		i = 0
		for bin in binArray:
			while not bin.isEmpty():
				intList[i] = bin.dequeue()
				i += 1
				
		# Advance to the next column value.
		column *= 10
	return intList