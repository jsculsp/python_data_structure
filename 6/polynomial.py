# Implementation of the Polynomial ADT using a sorted linked list.
class Polynomial(object):
	# Create a new polynomial object.
	def __init__(self, degree = None, coefficient = None):
		if degree is None:
			self._polyHead = None
		else:
			self._polyHead = _PolyTermNode(degree, coefficient)
		self._polyTail = self._polyHead
		
	# Run the degree of the polynomial.
	def degree(self):
		if self._polyHead is None:
			return -1
		else:
			return self._polyHead.degree
			
	# Return the coefficient for the term of the given degree.
	def __getitem__(self, degree):
		assert self.degree() >= 0, \
			'Operation is not permitted on an empty polynomial.'
		curNode = self._polyHead
		while curNode is not None and curNode.degree > degree:
			curNode = curNode.next
			
		if curNode is None or curNode.degree != degree:
			return 0.0
		else:
			return curNode.coefficient
			
	# Evaluate the polynomial at the given scalar value.
	def evaluate(self, scalar):
		assert self.degree() >= 0, \
			'Only non-empty polynomials can be evaluated.'
		result = 0.0
		curNode = self._polyHead
		while curNode is not None:
			result += curNode.coefficient * (scalar ** curNode.degree)
			curNode = curNode.next
		return result
		
	# Polynomial addition: newPoly = self + rhsPoly.
	def __add__(self, rhsPoly):
		assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
			'Addition only allowed on non-empty polynomials.'
		
		newPoly = Polynomial()
		nodeA = self._polyHead
		nodeB = rhsPoly._polyHead
		
		# Add corresponding terms until one list is empty.
		while nodeA is not None and nodeB is not None:
			if nodeA.degree > nodeB.degree:
				degree = nodeA.degree
				value = nodeA.coefficient
				nodeA = nodeA.next
			elif nodeA.degree < nodeB.degree:
				degree = nodeB.degree
				value = nodeB.coefficient
				nodeB = nodeB.next
			else:
				degree = nodeA.degree
				value = nodeA.coefficient + nodeB.coefficient
				nodeA = nodeA.next
				nodeB = nodeB.next
			newPoly._appendTerm(degree, value)
			
		# If self list contains more terms, append them.
		while nodeA is not None:
			newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
			nodeA = nodeA.next
			
		# Or if rhsPoly contains more terms, append them.
		while nodeB is not None:
			newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
			nodeB = nodeB.next
			
		return newPoly
		
	# Polynomial substraction: newPoly = self - rhsPoly.
	def __sub__(self, rhsPoly):
		assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
			'Substraction only allowed on non-empty polynomials.'
		
		newPoly = Polynomial()
		nodeA = self._polyHead
		nodeB = rhsPoly._polyHead
		
		# Add corresponding terms until one list is empty.
		while nodeA is not None and nodeB is not None:
			if nodeA.degree > nodeB.degree:
				degree = nodeA.degree
				value = nodeA.coefficient
				nodeA = nodeA.next
			elif nodeA.degree < nodeB.degree:
				degree = nodeB.degree
				value = -nodeB.coefficient
				nodeB = nodeB.next
			else:
				degree = nodeA.degree
				value = nodeA.coefficient - nodeB.coefficient
				nodeA = nodeA.next
				nodeB = nodeB.next
			newPoly._appendTerm(degree, value)
			
		# If self list contains more terms, append them.
		while nodeA is not None:
			newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
			nodeA = nodeA.next
			
		# Or if rhsPoly contains more terms, append them.
		while nodeB is not None:
			newPoly._appendTerm(nodeB.degree, -nodeB.coefficient)
			nodeB = nodeB.next
			
		return newPoly
		
	# Polynomial multiplication: newPoly = self * rhsPoly.
	def __mul__(self, rhsPoly):
		assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
			'Multiplication only allowed on non-empty polynomials.'
			
		# Create a new polynomial by multiplying rhsPoly by the first term.
		node = self._polyHead
		newPoly = rhsPoly._termMultiply(node)
		
		# Iterate through the remaining terms of the poly computing
		# the product of the rhsPoly by each term.
		node = node.next
		while node is not None:	
			tempPoly = rhsPoly._termMultiply(node)
			newPoly = newPoly.__add__(tempPoly)
			node = node.next
			
		return newPoly
		
	# Helper method for creating a new polynomial from multiplying an
	# existing polynomial by another term.
	def _termMultiply(self, termNode):
		newPoly = Polynomial()
		
		# Iterate through the terms and compute the product of each term and
		# the term in termNode.
		curNode = self._polyHead
		while curNode is not None:
			# Compute the product of the terms.
			newDegree = curNode.degree + termNode.degree
			newCoeff = curNode.coefficient * termNode.coefficient
			
			# Append it to the new polynomial.
			newPoly._appendTerm(newDegree, newCoeff)
			
			# Advance the current pointer.
			curNode = curNode.next
		return newPoly
		
	# Helper method for appending terms to the polynomial.
	def _appendTerm(self, degree, coefficient):
		if coefficient != 0:
			newTerm = _PolyTermNode(degree, coefficient)
			if self._polyHead is None:
				self._polyHead = newTerm
			else:
				self._polyTail.next = newTerm
			self._polyTail = newTerm
				
# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
	def __init__(self, degree, coefficient):
		self.degree = degree
		self.coefficient = coefficient
		self.next = None