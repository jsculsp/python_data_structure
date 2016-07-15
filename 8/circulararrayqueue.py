# Implementation of the Queue ADT using a circular array.
from my_own_array import Array

class Queue(object):
	# Creates an empty queue.
	def __init__(self, maxSize):
		self._count = 0
		self._front = 0
		self._back = maxSize - 1
		self._qArray = Array(maxSize)
		
	# Returns True if the queue is empty.
	def isEmpty(self):
		return self._count == 0
		
	# Returns True if the queue is full.
	def isFull(self):
		return self._count == len(self._qArray)
		
	# Adds the given item to the queue.
	def enqueue(self, item):
		assert not self.isFull(), 'Cannot enqueue to a full queue.'
		maxSize = len(self._qArray)
		self._back = (self._back + 1) % maxSize
		self._qArray[self._back] = item
		self._count += 1
		
	def dequeue(self):
		assert not self.isEmpty(), 'Cannot dequeue from a empty queue.'
		item = self._qArray[self._front]
		maxSize = len(self._qArray)
		self._front = (self._front + 1) % maxSize
		self._count -= 1
		