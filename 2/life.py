# Implements the LifeGrid ADT for use with the game of life.
from my_own_array import Array2D

class LifeGrid(object):
	# Defines constants to represent the cell states.
	DEAD_CELL = 0
	LIVE_CELL = 1
	
	# Creates the game grid and initializes the cells to dead.
	def __init__(self, 	numRows, numCols):
		# Allocate the 2-D array for the grid.
		self._grid = Array2D(numRows, numCols)
		# Clear the grid and set all cells to dead.
		self.configure(list())
		
	# Returns the number of rows in the grid.
	def numRows(self):
		return self._grid.numRows()
		
	# Returns the number of columns in the grid.
	def numCols(self):
		return self._grid.numCols()
		
	# Configures the grid to contain the given live cell.
	def configure(self, coordList):
		# Clear the game grid.
		for i in range(self.numRows()):
			for j in range(self.numCols()):
				self.clearCell(i, j)
				
		# Set the indicated cells to be alive.
		for coord in coordList:
			self.setCell(coord[0], coord[1])
			
	# Does the indicated cell contain a live organism?
	def isLiveCell(self, row, col):
		return self._grid[row, col] == LifeGrid.LIVE_CELL

	# Clears the indicated cell by setting it to dead.
	def clearCell(self, row, col):
		self._grid[row, col] = LifeGrid.DEAD_CELL
		
	# Sets the indicated cell to be alive.
	def setCell(self, row, col):
		self._grid[row, col] = LifeGrid.LIVE_CELL
		
	# Returns the number of live neighbors for the given cell.
	def numLiveNeighbors(self, row, col):
		# Creates a temporary grid extending the border by  1 cell each direction.
		temp_grid = LifeGrid(self.numRows() + 2, self.numCols() + 2)
		temp_list = []
		for i in range(self.numRows()):
			for j in range(self.numCols()):
				if self._grid[i, j] == 1:
					temp_list.append((i + 1, j + 1))
		temp_grid.configure(temp_list)
		
		# Returns the number of live neighbors for the given cell.
		live_num = 0
		for i in range(row , row + 3):
			for j in range(col, col + 3):
				live_num += temp_grid[i, j]
		live_num -= temp_grid[row + 1, col + 1]
		return live_num
	def __getitem__(self, index):
		return self._grid.__getitem__(index)