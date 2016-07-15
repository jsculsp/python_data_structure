# Sorts a sequence in asending order using the bubble sort algorithm.
def bubbleSort(theSeq):
	n = len(theSeq)
	# Perform n-1 bubble operations on the sequence.
	for i in range(n - 1):
		# Bubble the largest item to the end.
		if_changed = 0
		for j in range(n - 1 - i):
			if theSeq[j] > theSeq[j + 1]:	# swap the j and j+1 items.
				theSeq[j], theSeq[j + 1] = theSeq[j + 1], theSeq[j]
				if_changed = 1
		if if_changed == 0:
			break