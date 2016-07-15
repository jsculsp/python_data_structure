# Program for playing the game of Life.
from life import LifeGrid
from random import randrange

# Define the initial configuration of live cells.
INIT_CONFIG = [(randrange(10), randrange(10)) for i in range(50)]

# Set the size of the grid.
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Indicate the number of generations.
NUM_GENS = 20	

def main():
	# Construct the game grid and configure it.
	grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
	grid.configure(INIT_CONFIG)
	
	# Play the game.
	print('This is the initial generation: ')
	draw(grid)
	for i in range(NUM_GENS):
		print('This is generation %s: ' % (i + 1))
		evolve(grid)
		draw(grid)

# Generates the next generation of organisms.		
def evolve(grid):
	# List for storing the live cells of the next generations.
	liveCells = list()
	
	# Iterate over the elements of the grid.
	for i in range(grid.numRows()):
		for j in range(grid.numCols()):
			
			# Determine the number of live neighbors for this cell.
			neighbors = grid.numLiveNeighbors(i, j)
			
			# Add the (i, j) tuple to liveCells if this cell contains
			# a live organism in the next generation.
			if (neighbors == 2 and grid.isLiveCell(i, j)) or \
				(neighbors == 3):
				liveCells.append((i, j))
				
	# Reconfigure the grid using the liveCells coord list.
	grid.configure(liveCells)
	
# Prints a text-based representation of the game grid.
def draw(grid):
	for i in range(grid.numRows()):
		for j in range(grid.numCols()):
			print grid[i, j],
		print ''
	print '\n\n'

# Executes the main routine
if __name__ == '__main__':
	main()