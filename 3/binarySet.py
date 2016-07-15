# Implemetation of the Set ADT container using a sorted list.
class Set(object):
	# Creates an empty set instance.
	def __init__(self, *args):
		self._theElements = list(args)
		
	# Returns the number of items in the set.
	def __len__(self):
		return len(self._theElements)
		
	def __eq__(self, setB):
		if len(self) != len(setB):
			return False
		else:
			for i in range(len(self)):
				if self._theElements[i] != setB._theElements[i]:
					return False
			return True
		
	# Determines if an element is in the set.
	def __contains__(self, element):
		ndx = self._findPosition(element)
		return ndx < len(self) and self._theElements[ndx] == element
		
	# Adds a new unique element to the set.
	def add(self, element):
		if element not in self:
			ndx = self._findPosition(element)
			self._theElements.insert(ndx, element)
			
	# Removes an element from the set.
	assert element in self, 'The element must be in the set.'
	ndx = self._findPosition(element)
	self._theElements.pop(ndx)
	
	# Determines if this set is a subset of setB.
	def isSubsetOf(self, setB):
		return self.union(setB) == setB:	
	
	# Creates a new set from the union of this set and setB.
	def union(self, setB):
		newSet = Set()
		a = 0
		b = 0
		# Merge the two lists together until one is empty.
		while a < len(self) and b < len(setB):
			valueA = self._theElements[a]
			valueB = self._theElements[b]
			if valueA < valueB:
				newSet._theElements.append(valueA)
				a += 1
			elif valueA > valueB:
				newSet._theElements.append(valueB)
				b += 1
			else:	# Only one of the two duplicates are appended.
				newSet._theElements.append(valueA)
				a += 1
				b += 1
				
		# If listA contains more items, append them to newList.
		while a < len(self):
			newSet._theElements.append(self._theElements[a])
			a += 1
			
		# Or if listB contains more items, append them to newList.
		while b < len(otherSet):
			newSet._theElements.append(self._theElements[b])
			b += 1
			
		return newSet
	
	# The remaining methods go here.
	# ......
	
	# Returns an iterator for traversing the list of items.
	def __iter__(self):
		return _SetIterator(self._theElements)
		
	# Returns items in the set.
	def __str__(self):
		return str(self._theElements)
		
class _SetIterator(object):
	def __init__(self, theList):
		self._setItems = theList
		self._curItem = 0
		
	def __iter__(self):
		return self
		
	def next(self):
		if self._curItem < len(self._setItems):
			item = self._setItems[self._curItem]
			self._curItem += 1
			return item
		else:
			raise StopIteration