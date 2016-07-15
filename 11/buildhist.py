# Prints a histogram for a distribution of the letter grades computed
# from a collection of numeric grades extracted from a text file.

from maphist import Histogram

def main():
	# Create a Histogram instance for computing the frequencies.
	gradeHist = Histogram('ABCDF')
	
	# Open the text file containing the grades.
	with open('cs101grades.txt') as gradeFile:
		content = gradeFile.readlines()
	
	# Extract the grades and increment the appropriate counter.
	lst = []
	for line in content:
		lst += line.split(' ')
	for i in lst:
		grade = int(i)
		gradeHist.incCount(letterGrade(grade))
	
	# Print the histogram chart.
	printChart(gradeHist)
	
# Determine the letter grade for the given numeric value.
def letterGrade(grade):
	if grade >= 90:
		return 'A'
	elif grade >= 80:
		return 'B'
	elif grade >= 70:
		return 'C'
	elif grade >= 60:
		return 'D'
	else:
		return 'F'
		
# Print the histogram as a horizontal bar chart.
def printChart(gradeHist):
	print('		Grade Distribution.')
	# Print the body of the chart.
	letterGrades = ('A', 'B', 'C', 'D', 'F')
	for letter in letterGrades:
		print('  |')
		print(letter + ' +'),
		freq = gradeHist.getCount(letter)
		print('*' * freq)
		
	# Print the x-axis.
	print('  |')
	print(' ' + '+----' * 8)
	print(' 0    5    10   15   20   25   30   35')
	
# Call the main routine.	
if __name__ == '__main__':
	main()