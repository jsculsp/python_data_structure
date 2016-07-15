# Sorts a virtual subsequence in ascending order using merge sort.

from my_own_array import Array

def recMergeSort(theSeq, first, last, tmpArray):
	# The elements that comprise the virtual subsequence are indicated
	# by the range [first...last]. tmpArray is temporary storage used in
	# the merging phase of the merge sort algorithm.
	
	# Check the base case: the virtual sequence contains a single item.
	if first == last:
		return theSeq
	else:
		# Compute the mid point.
		mid = (first + last) // 2
		
		# Split the sequence and perform the recursive step.
		recMergeSort(theSeq, first, mid, tmpArray)
		recMergeSort(theSeq, mid+1, last, tmpArray)
		
		# Merge the two ordered subsequences.
		mergeVirtualSeq(theSeq, first, mid+1, last+1, tmpArray)
		
# Merges the two sorted virtual subsequences: [left..right) [right..end)
# using the tmpArray for intermediate storage.
def mergeVirtualSeq(theSeq, left, right, end, tmpArray):
	# Initialize two subsequence index variables.
	a = left
	b = right
	# Initialize an index variables for the resulting merged array.
	m = 0
	# Merge the two sequences together until one is empty.
	while a < right and b < end:
		if theSeq[a] < theSeq[b]:
			tmpArray[m] = theSeq[a]
			a += 1
		else:
			tmpArray[m] = theSeq[b]
			b += 1
		m += 1
		
	# If the left subsequence contains more items append them to tmpArray.
	while a < right:
		tmpArray[m] = theSeq[a]
		a += 1
		m += 1
		
	# Or if right subsequence contains more, append them to tmpArray.
	while b < end:
		tmpArray[m] = theSeq[b]
		b += 1
		m += 1
		
	# Copy the sorted subsequence back into the original sequence structure.
	for i in range(end - left):
		theSeq[i + left] = tmpArray[i]
		
	return theSeq
		
# Sort an array or list in ascending order using merge sort.
def mergeSort(theSeq):
	n = len(theSeq)
	# Create a temporary array for use when merging subsequences.
	tmpArray = Array(n)
	# Call the private recursive merge sort function.
	recMergeSort(theSeq, 0, n-1, tmpArray)
	return theSeq