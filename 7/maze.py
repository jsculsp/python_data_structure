# Implements the Maze ADT using a 2-D array.
from my_own_array import Array2D
from linkliststack import Stack

class Maze(object):
	# Define constants to represent contents of the maze cells.
	MAZE_WALL = '*'
	PATH_TOKEN = 'x'
	TRIED_TOKEN = 'o'
	
	# Create a maze object with all cells marked as open.
	def __init__(self, numRows, numCols):
		self._mazeCells = Array2D(numRows, numCols)
		self._startCell = None
		self._exitCell = None
		
	# Returns the number of rows in the maze.
	def numRows(self):
		return self._mazeCells.numRows()
		
	# Returns the number of cols in the maze.
	def numCols(self):
		return self._mazeCells.numCols()
		
	# Fills the indicated cell with a 'wall' marker.
	def setWall(self, row, col):
		assert row >= 0 and row < self.numRows() and \
			col >= 0 and col < self.numCols(), 'Cell index out of range.'
		self._mazeCells.__setitem__((row, col), self.MAZE_WALL)
		
	# Sets the starting cell position.
	def setStart(self, row, col):
		assert row >= 0 and row < self.numRows() and \
			col >= 0 and col < self.numCols(), 'Cell index out of range.'
		self._startCell = _CellPosition(row, col)
		
	# Sets the exit cell position.
	def setExit(self, row, col):
		assert row >= 0 and row < self.numRows() and \
			col >= 0 and col < self.numCols(), 'Cell index out of range.'
		self._exitCell = _CellPosition(row, col)
		
	# Attempts to solve the maze by finding a path from the starting cell
	# to the exit. Returns True if a path is found and False otherwise.
	def findPath(self):
		stack = Stack()
		curRow, curCol = self._startCell.row, self._startCell.col
		i = 1
		while True:
			if self._exitFound(curRow, curCol):
				self._markPath(curRow, curCol)
				return True
			else:
				self._markPath(curRow, curCol)
			
			find_a_way = 0
			for direction in ((curRow - 1, curCol), (curRow + 1, curCol),
							(curRow, curCol - 1), (curRow, curCol + 1)):
				if self._validMove(direction[0], direction[1]):
					curPosition = _CellPosition(curRow, curCol)
					stack.push(curPosition)
					curRow, curCol = direction[0], direction[1]
					find_a_way = 1
					break
							
			if find_a_way == 0:
				self._markTried(curRow, curCol)
				curPosition = stack.pop()
				if curPosition == self._startCell:
					return False
				curRow, curCol = curPosition.row, curPosition.col
			print('This is the %s attempt...\n' % i)
			i += 1
		
		
	# Reset the maze by removing all 'path' and 'tried' tokens.
	def reset(self):
		for i in range(self.numRows()):
			for j in range(self.numCols()):
				if self._mazeCells[i, j] == 'x' or self._mazeCells[i, j] == 'o':
					self._mazeCells[i, j] = None
		
	# Prints a text-based representation of the maze.
	def draw(self):
		for i in range(self.numRows()):
			for j in range(self.numCols()):
				if self._mazeCells[i, j] == None:
					print ' ',
				elif i == self._startCell.row and j == self._startCell.col:
					print 'S',
				elif i == self._exitCell.row and j == self._exitCell.col:
					print 'E',
				else:
					print self._mazeCells[i, j],
			print ''
		
	# Returns True if the given cell position is a valid move.
	def _validMove(self, row, col):
		return row >= 0 and row < self.numRows() and \
			col>= 0 and col < self.numCols() and \
			self._mazeCells[row, col] is None
			
	# Helper method to determine if the exit was found.
	def _exitFound(self, row, col):
		return row == self._exitCell.row and \
			col == self._exitCell.col
			
	# Drops a 'tried' token at the given cell.
	def _markTried(self, row, col):
		self._mazeCells[row, col] = self.TRIED_TOKEN
		
	# Drops a 'path' token at the given cell.
	def _markPath(self, row, col):
		self._mazeCells[row, col] = self.PATH_TOKEN	
		
# Private storage class for holding a cell position.
class _CellPosition(object):
	def __init__(self, row, col):
		self.row = row
		self.col = col