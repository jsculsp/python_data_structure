# Implements the Bag ADT using a singly linked list.

class Bag(object):
	# Constructs an empty bag.
	def __init__(self):
		self._head = None
		self._size = 0
		
	# Return the number of items in the bag.
	def __len__(self):
		return self._size
		
	# Determines if an item is contained in the bag.
	def __contains__(self, target):
		curNode = self._head
		while curNode is not None and curNode._item != target:
			curNode = curNode._next
		return curNode is not None
		
	# Adds a new item to the bag.
	def add(self, item):
		newNode = _BagListNode(item)
		newNode._next = self._head
		self._head = newNode
		self._size += 1
		
	# Removes an instance of the item from the bag.
	def remove(self, item):
		preNode = None
		curNode = self._head
		while curNode is not None and curNode._item != item:
			preNode = curNode
			curNode = curNode._next
			
		# The item has to be in the bag to remove it.
		assert curNode is not None, 'The item must be in the bag.'
		
		# Unlink the node and return the item.
		self._size -= 1
		if curNode == self._head:
			self._head = curNode._next
		else:
			preNode._next = curNode._next
		return curNode._item
		
	# Returns an iterator for traversing the list of item.
	def __iter__(self):
		return _BagIterator(self._head)
		
# An iterator for the Bag ADT.
class _BagIterator(object):
	def __init__(self, head):
		self._curItem = head
		
	def __iter__(self):
		return self
		
	def next(self):
		if self._curItem != None:
			item = self._curItem._item
			self._curItem = self._curItem._next
			return item
		else:
			raise StopIteration	
	
# Define a private storage class for creating list nodes.
class _BagListNode(object):
	def __init__(self, item):
		self._item = item
		self._next = None