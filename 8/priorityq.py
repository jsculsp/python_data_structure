# Implementation of the unbounded Priority Queue ADT using a Python list
# with new items append to the end.
class PriorityQueue(object):
	# Create an empty unbounded priority queue.
	def __init__(self):
		self._qList = list()
		
	# Return True if the queue is empty.
	def isEmpty(self):
		return len(self) == 0
		
	# Return the number of items in the queue.
	def __len__(self):
		return len(self._qList)
		
	# Add the given item to the queue.
	def enqueue(self, item, priority):
		# Create a new instance of the storage class and append it to the list.
		entry = _PriorityQEntry(item, priority)
		self._qList.append(entry)
		
	# Remove and return the first item in the queue.
	def dequeue(self):
		assert not self.isEmpty(), 'Cannot dequeue from an empty queue.'
		
		# Find the entry with the highest priority.
		highest = self._qList[0].priority
		for i in range(self.len()):
			# See if the ith entry contains a higher priority (smaller integer).
			if self._qList[i].priority < highest:
				highest = self._qList[i].priority
				
		# Remove the entry with the highest priority and return the item.
		entry = self._qList.pop(highest)
		return entry.item
		
# Private storage class for associating queue items with their priority.
class _PriorityQEntry(object):
	def __init__(self, item, priorty):
		self.item = item
		self.priority = priority