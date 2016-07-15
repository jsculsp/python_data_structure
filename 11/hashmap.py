# Implementation of the Map ADT using closed hashing and a probe
# with double hashing.
from my_own_array import Array

class HashMap(object):
	# Defines constants to represent the status of each table entry.
	# UNUSED = None
	# EMPTY = _MapEntry(None, None)
	
	# Creates an empty map instance.
	def __init__(self):
		self.UNUSED = None
		self.EMPTY = _MapEntry(None, None)
		self._table = Array(7)
		self._count = 0
		self._maxCount = len(self._table) - len(self._table) // 3
		
	# Returns the number of entries in the map.
	def __len__(self):
		return self._count
		
	# Determines if the map contains the given key.
	def __contains__(self, key):
		slot = self._findSlot(key, False)
		return slot is not None
	
	# Adds a new entry to the map if the key does not exist. Otherwise,
	# the new value replaces the current value associated with the key.
	def add(self, key, value):
		if key in self:
			slot = self._findSlot(key, False)
			self._table[slot].value = value
			return False
		else:
			slot = self._findSlot(key, True)
			self._table[slot] = _MapEntry(key, value)
			self._count += 1
			if self._count == self._maxCount:
				self._rehash()
			return True
			
	# Returns the value associated with the key.
	def valueOf(self, key):
		slot = self._findSlot(key, False)
		assert slot is not None, 'Invalid map key.'
		return self._table[slot].value
		
	# Removes the entry associated with the key.
	def remove(self, key):
		slot = self._findSlot(key, False)
		assert slot is not None, 'Invalid map key.'
		self._table[slot] = self.EMPTY
		self._count -= 1
		
	# Returns an iterator for traversing the keys in the map.
	def __iter__(self):
		return _MapIterator(self._table)
	
	# Finds the slot containing the key or where the key can be added.
	# forInsert indicates if the search is for an insertion, which locates
	# the slot into which the new key can be added.
	def _findSlot(self, key, forInsert):
		# Compute the home slot and the step size.
		slot = self._hash1(key)
		step = self._hash2(key)
		
		# Probe for the key.
		M = len(self._table)
		while True:
			if forInsert and \
				(self._table[slot] is self.UNUSED or self._table[slot] is self.EMPTY):
				return slot	
			elif not forInsert and self._table[slot] is not self.UNUSED and \
				(self._table[slot] is not self.EMPTY and self._table[slot].key == key):
				return slot
			elif not forInsert and self._table[slot] is self.UNUSED:
				return None
			else:
				slot = (slot + step) % M
		
	# Rebuilds the hash table.
	def _rehash(self):
		# Create a new larger table.
		origTable = self._table
		newSize = len(self._table) * 2 + 1
		self._table = Array(newSize)
		
		# Modify the size attributes.
		self._count = 0
		self._maxCount = newSize - newSize // 3
		
		# Add the keys from the original array to the new table.
		for entry in origTable:
			if entry is not self.UNUSED and entry is not self.EMPTY:
				slot = self._findSlot(entry.key, True)
				self._table[slot] = entry
				self._count += 1
		
	# The main hash function for mapping keys to table entries.
	def _hash1(self, key):
		return abs(hash(key)) % len(self._table)
		
	# The second hash function used with double hashing probes.
	def _hash2(self, key):
		return 1 + abs(hash(key)) % (len(self._table) - 2)

# Storage class for holding the key/value pairs.		
class _MapEntry(object):
	def __init__(self, key, value):
		self.key = key
		self.value = value
		
class _MapIterator(object):
	def __init__(self, theTable):
		self._table = theTable
		for i in range(len(self._table)):
			if self._table[i] is not None and \
				self._table[i].key != None:
				self._curNdx = i
				break
		
	def __iter__(self):
		return self
		
	def next(self):
		if self._curNdx < len(self._table):
			entry = self._table[self._curNdx]
			self._curNdx += 1
			while self._curNdx < len(self._table) and \
				(self._table[self._curNdx] is None or \
				self._table[self._curNdx].key == None):
				self._curNdx += 1
			if entry is not None and entry.key != None:
				return (entry.key, entry.value)
		else:
			raise StopIteration