# Implementation of the Sparse Matrix ADT using a list.

class SparseMatrix(object):
	# Create a sparse matrix of size numRows * numCols initialized to 0.
	def __init__(self, numRows, numCols):
		self._numRows = numRows
		self._numCols = numCols
		self._elementList = list()
		
	# Return the number of rows in the matrix.
	def numRows(self):
		return self._numRows
		
	# Return the number of cols in the matrix.
	def numCols(self):
		return self._numCols
		
	# Return the value of element (i, j): x[i, j]
	def __getitem__(self, ndxTuple):
		assert len(ndxTuple) == 2, 'Invalid number of array subscript.'
		ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
		if ndx is not None:
			return self._elementList[ndx].value
		else:
			return 0
		
	# Set the value of element (i, j) to the value s: x[i, j] = s
	def __setitem__(self, ndxTuple, scalar):
		assert len(ndxTuple) == 2, 'Invalid number of array subscript.'
		ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
		if ndx is not None:		# if the element is found in the list.
			if scalar != 0.0:
				self._elementList[ndx].value = scalar
			else:
				self._elementList.pop(ndx)
		else:
			if scalar != 0.0:	# if the element is zero and not in the list.
				element = _MatrixElement(ndxTuple[0], ndxTuple[1], scalar)
				self._elementList.append(element)
				
	# Create and return a new sparse matrix that results from matrix addition.
	def __add__(self, rhsMatrix):
		assert rhsMatrix.numRows() == self.numRows() and \
			rhsMatrix.numCols() == self.numCols(), \
			'Matrix sizes not compatible for the operation.'
			
		# Create the new matrix.
		newMatrix = SparseMatrix(self.numRows(), self.numCols())
		
		# Duplicate the lhs matrix. The elements are mutable, thus we must
		# create new objects and not simply copy the reference.
		for element in self._elementList:
			dupElement = _MatrixElement(element.row, element.col, element.value)
			newMatrix._elementList.append(dupElement)
			
		# Iterate through each non-zero element of the rhsMatrix.
		for element in rhsMatrix._elementList:
			# Get the value of the corresponding element in the new matrix.
			value = self[element.row, element.col]
			value += element.value
			#Store the new value back to the new matrix.
			newMatrix[element.row, element.col] = value
			
		# return the new matrix.
		return newMatrix
		
	# Create and return a new sparse matrix that results from matrix subtraction.
	def __sub__(self, rhsMatrix):
		newMatrix = SparseMatrix(rhsMatrix.numRows(), rhsMatrix.numCols())
		for element in rhsMatrix._elementList:
			dupElement = _MatrixElement(element.row, element.col, -element.value)
			newMatrix._elementList.append(dupElement)
		return self.__add__(newMatrix)
			
		
	# Create and return a new sparse matrix that results from matrix multiplication.
	def __mul__(self, rhsMatrix):
		assert self.numCols() == rhsMatrix.numRows(), \
			'Columns of the first matrix are not equal to rows 	of the second.'
		
		# Create the new matrix.
		newMatrix = SparseMatrix(self.numRows(), rhsMatrix.numCols())
			
		# Creates and returns a new matrix resulting from matrix multiplication.
		for i in range(self.numRows()):
			for j in range(rhsMatrix.numCols()):
				for k in range(self.numCols()):
					newMatrix[i, j] += self[i, k] * rhsMatrix[k, j]
		
		# Return the new matrix
		return newMatrix
	
	# Scale the matrix by the given scalar.
	def scaleBy(self, scalar):
		for element in self._elementList:
			element.value *= scalar
			
	
	# Helper method used to find a specific matrix element (row, col) in the 
	# list of non-zero entries. None is returned if the element is not found.
	def _findPosition(self, row, col):
		assert 0 <= row < self.numRows() and \
			0 <= col < self.numCols(), 'Matrix subscript out of range.'
		n = len(self._elementList)
		for i in range(n):
			if row == self._elementList[i].row and \
				col == self._elementList[i].col:
				return i	# return the index of the element if found.
		return None			# return None when the element is zero.
		
	# Storage class for holding the non-zero matrix elements.
class _MatrixElement(object):
	def __init__(self, row, col, value):
		self.row = row
		self.col = col
		self.value = value
			