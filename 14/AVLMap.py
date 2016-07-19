from linkliststack import Stack

# Constants for the balance factors.
LEFT_HIGH = 1
EQUAL_HIGH = 0
RIGHT_HIGH = -1

# Implementation of the map ADT using an AVL tree.
class AVLMap(object):
	def __init__(self):
		self._root = None
		self._size = 0
		
	def __len__(self):
		return self._size
		
	def __contains__(self, key):
		return self._bstSearch(self._root, key) is not None
		
	# Returns an iterator for traversing the keys in the map.
	def __iter__(self):
		return _BSTMapIterator(self._root)
		
	def add(self, key, value = None):
		node = self._bstSearch(self._root, key)
		if node is not None:
			node.value = value
			return False
		else:
			(self._root, tmp) = self._avlInsert(self._root, key, value)
			self._size += 1
			return True
			
	def valueOf(self, key):
		node = self._bstSearch(self._root, key)
		assert node is not None, 'Invalid map key.'
		return node.value
		
	def __getitem__(self, key):
		return self.valueOf(key)
		
	def __setitem__(self, key, value):
		self.add(key, value)
		
	def remove(self, key):
		assert key in self, 'Invalid map key.'
		(self._root, tmp) = self.avlRemove(self._root, key)
		self._size -= 1
		
	def __iter__(self):
		return _AVLMapIterator(self._root)
		
	# Helper method that recursively searches the tree for a target key.
	def _bstSearch(self, subtree, target):
		if subtree is None:			# base case.
			return None
		elif target < subtree.key:	# target is left of the subtree root.
			return self._bstSearch(subtree.left, target)
		elif target > subtree.key:	# target is right of the subtree root.
			return self._bstSearch(subtree.right, target)
		else:
			return subtree
			
	# Rotates the pivot to the right around its left child.
	def _avlRotateRight(self, pivot):
		C = pivot.left
		pivot.left = C.right
		C.right = pivot
		return C
		
	# Rotates the pivot to the left around its right child.
	def _avlRotateLeft(self, pivot):
		C = pivot.right
		pivot.right = C.left
		C.left = pivot
		return C
		
	# Rebalance a node with its left subtree is higher.
	def _avlLeftBalance(self, pivot):
		# Set C to point the left child of the pivot.
		C = pivot.left
		# See if the rebalancing is due to case 1.
		if C.bfactor == LEFT_HIGH:
			pivot.bfactor = EQUAL_HIGH
			C.bfactor = EQUAL_HIGH
			pivot = self._avlRotateRight(pivot)
			return pivot
			
		# Otherwise, a balance from the left is due to case 2.
		elif C.bfactor == RIGHT_HIGH:
			# Set G to point the right child of C.
			G = C.right
			# Change the balance factors.
			if G.bfactor == LEFT_HIGH:
				pivot.bfactor = RIGHT_HIGH
				C.bfactor = EQUAL_HIGH
				G.bfactor = EQUAL_HIGH
			elif G.bfactor == RIGHT_HIGH:
				pivot.bfactor = EQUAL_HIGH
				C.bfactor = LEFT_HIGH
				G.bfactor = EQUAL_HIGH
				
			# Perform the double rotation.
			C = self._avlRotateLeft(C)
			pivot = self._avlRotateRight(pivot)
			return pivot
			
	# Rebalance a node with its right subtree is higher.
	def _avlRightBalance(self, pivot):
		# Set C to point to the right child of the pivot.
		C = pivot.right
		
		# See if the rebalancing is due to case 3.
		if C.bfactor == RIGHT_HIGH:
			pivot.bfactor = EQUAL_HIGH
			C.bfactor = EQUAL_HIGH
			pivot = self._avlRotateLeft(pivot)
			return pivot
			
		# Otherwise, a balance from the right is due to case 4.
		elif C.bfactor == LEFT_HIGH:
			G = C.left
		# Change the balance factors.
			if G.bfactor == LEFT_HIGH:
				pivot.bfactor = RIGHT_HIGH
				C.bfactor = EQUAL_HIGH
				G.bfactor = EQUAL_HIGH
			elif G.bfactor == RIGHT_HIGH:
				pivot.bfactor = EQUAL_HIGH
				C.bfactor = LEFT_HIGH
				G.bfactor = EQUAL_HIGH
				
			# Perform the double rotation.
			C = self._avlRotateRight(C)
			pivot = self._avlRotateLeft(pivot)
			return pivot
			
	# Recursive method to handle the insertion into an AVL tree. The
	# function returns a tuple containing a reference to the root of the
	# subtree and a boolean to indicate if the subtree grew taller.
	def _avlInsert(self, subtree, key, value):
		# See if we have found the insertion point.
		if subtree is None:
			subtree = _AVLMapNode(key, value)
			taller = True
			
		# Is the key already in the tree?
		elif key == subtree.key:
			return (subtree, False)
			
		# See if we need to navigate to the left.
		elif key < subtree.key:
			(node, taller) = self._avlInsert(subtree.left, key, value)
			subtree.left = node
			# If the subtree grew taller, see if it needs rebalancing.
			if taller:
				if subtree.bfactor == LEFT_HIGH:
					subtree = self._avlLeftBalance(subtree)
					taller = False
				elif subtree.bfactor == EQUAL_HIGH:
					subtree.bfactor = LEFT_HIGH
					taller = True
				else:
					subtree.bfactor = EQUAL_HIGH
					taller = False
		
		# Otherwise, navigate to the right.
		elif key > subtree.key:
			(node, taller) = self._avlInsert(subtree.right, key, value)
			subtree.right = node
			# If the subtree grew taller, see if it needs rebalancing.
			if taller:
				if subtree.bfactor == LEFT_HIGH:
					subtree.bfactor = EQUAL_HIGH
					taller = False
				elif subtree.bfactor == EQUAL_HIGH:
					subtree.bfactor = RIGHT_HIGH
					taller = True
				else:
					subtree = self._avlRightBalance(subtree)
					taller = False
					
		# Return the results.
		return (subtree, taller)
		
	def _avlRemove(subtree, target):
		# Search for the item in the tree.
		if subtree is None:
			return subtree
		elif target < subtree.key:
			subtree.left = self._avlRemove(subtree.left, target)
			
			
# An iterator for the binary search tree using a software stack.
class _BSTMAPIterator(object):
	def __init__(self, root):
		# Create a stack for use in traversing the tree.
		self._theStack = Stack()
		# We must traverse down to the node containing the smallest key
		# during which each node along the path is pushed onto the stack.
		self._traverseToMinNode(root)
		
	def __iter__(self):
		return self
		
	# Returns the next item from the BST in key order.
	def next(self):
		# If the stack is empty, we are done.
		if self._theStack.isEmpty():
			raise StopIteration
		else:
			# The top node on the stack contains the next key.
			node = self._theStack.pop()
			key = node.key
			# If this node has a subtree rooted as the right child, we must
			# find the node in that subtree that contains the smallest key.
			# Again, the nodes along the path are pushed onto the stack.
			if node.right is not None:
				self._traverseToMinNode(node.right)
			return key

	# Traverses down the subtree to find the node containing the smallest
	# key during which the nodes along that path are pushed onto the stack.
	def _traverseToMinNode(self, subtree):
		if subtree is not None:
			self._theStack.push(subtree)
			self._traverseToMinNode(subtree.left)
			
# Storage class for creating the AVL tree node.
class _AVLMapNode(object):
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.bfactor = EQUAL_HIGH
		self.left = None
		self.right = None
		
# An iterator for the binary search tree using a software stack.
class _AVLMapIterator(object):
	def __init__(self, root):
		# Create a stack for use in traversing the tree.
		self._theStack = Stack()
		# We must traverse down to the node containing the smallest key
		# during which each node along the path is pushed onto the stack.
		self._traverseToMinNode(root)
		
	def __iter__(self):
		return self
		
	# Returns the next item from the BST in key order.
	def next(self):
		# If the stack is empty, we are done.
		if self._theStack.isEmpty():
			raise StopIteration
		else:
			# The top node on the stack contains the next key.
			node = self._theStack.pop()
			key = node.key
			# If this node has a subtree rooted as the right child, we must
			# find the node in that subtree that contains the smallest key.
			# Again, the nodes along the path are pushed onto the stack.
			if node.right is not None:
				self._traverseToMinNode(node.right)
			return key

	# Traverses down the subtree to find the node containing the smallest
	# key during which the nodes along that path are pushed onto the stack.
	def _traverseToMinNode(self, subtree):
		if subtree is not None:
			self._theStack.push(subtree)
			self._traverseToMinNode(subtree.left)