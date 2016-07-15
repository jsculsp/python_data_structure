# Program for building and solving a maze.
from maze import Maze

# The main routine.
def main():
	maze = buildMaze('mazefile3.txt')
	if maze.findPath():
		print('Path found...')
		maze.draw()
	else:
		print('Path not found...')
		
# Builds a maze based on a text format in the given file.
def buildMaze(filename):
	with open(filename) as infile:
		# Read the size of the maze.
		nrows, ncols = readValuePair(infile)
		maze = Maze(nrows, ncols)
		
		# Read the starting and exiting positions.
		row, col = readValuePair(infile)
		maze.setStart(row, col)
		row, col = readValuePair(infile)
		maze.setExit(row, col)
		
		# Read the maze itself.
		for row in range(nrows):
			line = infile.readline()
			for col in range(len(line)):
				if line[col] == '*':
					maze.setWall(row, col)
		return maze

# Extracts an integer value pair from the given input file.		
def readValuePair(infile):
	line = infile.readline()
	valA, valB = line.split()
	return int(valA), int(valB)
	
if __name__ == '__main__':
	main()