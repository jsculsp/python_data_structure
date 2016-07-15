# implementation of the MultiArray ADT using a 1-D array.

from my_own_array import Array

class MultiArray(object):
	# Creates a multi-dimentional array.
	def __init__(self, *dimensions):
		assert len(dimensions) > 1, 'The array must have 2 or more dimensions.'
		# The variable argument tuple contaims the dim sizes.
		self._dims = dimensions
		# Compute the total number of elements in the array.
		size = 1
		for d in dimensions:
			assert d > 0, 'Demensions must be > 0.'
			size *= d
		
		# Create the 1-D array to store the elements.
		self._elements = Array(size)
		# Create a 1-D array to store the equation factors.
		self._factors = Array(len(dimensions))
		self._computeFactors()
		
	# Returns the number of dimensions in the array.
	def numDims(self):
		return len(self._dims)
		
	# Returns the length of the given dimention.
	def length(self, dim):
		assert dim >=1 and dim <= len(self._dims), \
			'Dimention component out of range.'
		return self._dims[dim - 1]
		
	# Clears the array by setting all elements to the given value.
	def clear(self, value):
		self._elements.clear(value)

	# Returns the contents of element(i_1, i_2, ..., i_n).
	def __getitem__(self, ndxTuple):
		assert len(ndxTuple) == self.numDims(), 'Invalid # of array subscripts.'
		index = self._computeIndex(ndxTuple)
		assert index is not None, 'Array subscript out of range.'
		return self._elements[index]
	
	# Sets the contents of element(i_1, i_2, ..., i_n).
	def __setitem__(self, ndxTuple, value):
		assert len(ndxTuple) == self.numDims(), 'Invalid # of array subscripts.'
		index = self._computeIndex(ndxTuple)
		assert index is not None, 'Array subscript out of range.'
		self._elements[index] = value
		
	# Computes the 1-D array offset for element (i_1, i_2, ..., i_n)
	# using the equation i_1 * f_1 + i_2 * f_2 + ... + i_n * f_n
	def _computeIndex(self, idx):
		offset = 0
		for j in range(len(idx)):
			# Make sure the imdex components are within the legal range.
			if idx[j] < 0 or idx[j] >= self._dims[j]:
				return None
			else: # Sum the product of i_j * f_j.
				offset += idx[j] * self._factors[j]
		return offset
		
	# Computes the factor values used in the index equation.
	def _computeFactors(self):
		for j in range(len(self._factors)):
			self._factors[j] = 1
			if j != len(self._factors) - 1:
				for i in range(j + 1, len(self._factors)):
					self._factors[j] *= self._dims[i]
		