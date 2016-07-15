# Sorts a linked list using merge sort. A new head reference is returned.
def llistMergeSort(theList):
	
	# If the list is empty (base case), return None.
	if theList is None:
		return None
	elif theList.next is None:
		return theList
		
	# Split the linked list into two sublists of equal size.
	rightList = _splitLinkedList(theList)
	leftList = theList
	
	# Perform the same operation on the left half...
	leftList = llistMergeSort(leftList)
	
	# Perform the same operation on the right half...
	rightList = llistMergeSort(rightList)
	
	# Merge the two ordered sublists
	theList = _mergeLinkedLists(leftList, rightList)
	
	# Return the head pointer of the ordered sublist.
	return theList
	
# Splits a linked list at the midpoint to create two sublists. The
# head reference of the right sublist is returned. The left sublist
# is still referenced by the original head reference.
def _splitLinkedList(subList):
	
	# Assign a reference to the first and second nodes in the list.
	midPoint = subList
	curNode = subList.next
	
	# Iterate through the list until curNode falls off the end.
	while curNode is not None:
		# Advance curNode to the next node.
		curNode = curNode.next
		
		# If there are more nodes, advance curNode again and midPoint once.
		if curNode is not None:
			curNode = curNode.next
			midPoint = midPoint.next
			
	# Set rightList as the head pointer to the right sublist.
	rightList = midPoint.next
	# Unlink the right sub list from the left sublist.
	midPoint.next = None
	# Return the right sub list head reference.
	return rightList
	
# Merge two sorted linked list; returns head reference for new list.
def _mergeLinkedLists(subListA, subListB):
	# Create a dummy node and insert it at the front of the list.
	newList = Node(None)
	newHead = newList
	
	# Append nodes to the new list until one list is empty.
	while subListA is not None and subListB is not None:
		if subListA.data <= subListB.data:
			newList.next = subListA
			subListA = subListA.next
		else:
			newList.next = subListB
			subListB = subListB.next
			
		newList = newList.next
		newList.next = None
	
	# If self list contains more items, append them.
	if subListA is not None:
		newList.next = subListA
	else:
		newList.next = subListB
		
	# Return the new merged list, which begins with the first node after
	# the dummy node.
	return newHead.next
	
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None