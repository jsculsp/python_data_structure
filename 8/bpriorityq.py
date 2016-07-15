# Implementation of the bounded Priority Queue ADT using an array of
# queues in witch the queues are implemented using a linked list.
from my_own_array import Array
from linklistqueue import Queue

class BPriorityQueue(object):
	# Creates an empty bounded priority queue.
	def __init__(self, numLevels):
		self._qSize = 0
		self._qLevels = Array(numLevels)
		for i in range(numLevels):
			self._qLevels[i] = Queue()
			
	# Return True if the queue is empty
	def isEmpty(self):
		return self._qSize == 0
		
	# Return the number of items in the queue.
	def __len__(self):
		return self._qSize
		
	# Add the given item to the queue.
	def enqueue(self, item, priority):
		assert priority >= 0 and priority < len(self._qLevels), \
			'Invalid priority level.'
		self._qLevels[priority].enqueue(item)
		
	# Remove and return the next item in the queue.
	def dequeue(self):
		# Make sure the queue is not empty.
		assert not self.isEmpty(), 'Cannot dequeue from an empty queue.'
		# Find the first non-empty queue.
		i = 0
		p = len(self._qLevels)
		while i < p and self._qLevels[i].isEmpty():
			i += 1
		# We know the queue is not empty, so dequeue from the ith queue.
		return self._qLevels[i].dequeue()