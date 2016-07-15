# Shows the creation of Eight-Queens Board and the Solving for Eight-Queens.

from sparsematrix import SparseMatrix

# Creates an n * n empty board.
class QueensBoard(object):
	def __init__(self, size):
		self._size = size
		self._board = SparseMatrix(size, size)
	
	# Returns the size of the board.
	def size(self):
		return self._size
		
	# Returns the number of queens currently positioned on the board.
	def numQueens(self):
		count = 0
		for i in range(self._size):
			for j in range(self._size):
				if self._board[i, j] == 1:
					count += 1
		return count
		
	# Returns a boolean value indicating if the given square 
	# is currently unguarded.
	def unguarded(self, row, col):
		for i in range(self._size):
			for j in range(self._size):
				if i == row or j == col or abs(i - row) == abs(j - col):
					if self._board[i, j] == 1:
						return False
		return True
		
	# Places a queen on the board at position (row, col).
	def placeQueen(self, row, col):
		self._board[row, col] = 1
		
	# Removes the queen from position(row, col).
	def removeQueen(self, row, col):
		self._board[row, col] = 0
		
	# Resets the board to its original state by removing all queens
	# currently placed on the board.
	def reset(self):
		self._board = SparseMatrix(self._size, self._size)
		
	# Prints the board in a readable format using characters to represent
	# the squares containing the queens and the empty squares.
	def draw(self):
		for i in range(self._size):
			for j in range(self._size):
				if self._board[i, j] == 0:
					print('*'),
				else:
					print('o'),
			print('')
		
def solveNQueens(board, col):	
	# A solution was found if n-queens have been placed on the board.
	if board.numQueens() == board.size():
		return True
	else:
		# Find the next unguarded square within this column.
		for row in range(board.size()):
			if board.unguarded(row, col):
				# Place a queen in that square.
				board.placeQueen(row, col)
				# Continue placing queens in the following columns.
				if solveNQueens(board, col + 1):
					# We are finished if a solution ws found.
					return True
				else:
					# No solution was found with the queen in this square, 
					# so it has be removed from the board.
					board.removeQueen(row, col)
					
		# If the loop terminates, no queen can be placed within this column.
		return False