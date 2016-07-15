from my_own_array import Array2D

# Open the text file for reading.
with open('examgrades.txt') as gradeFile:
	content = gradeFile.readlines()
	
numStudents = int(content[0])
numExams = int(content[1])
	
# Create the 2-D array to store the grades.
examGrades = Array2D(numStudents, numExams)

# Extract the grades from the remaining lines.
i = 0
for student in content[2:]:
	grades = student.split()
	for j in range(numExams):
		examGrades[i, j] = int(grades[j])
	i += 1
	
# Compute each student's average exam grade.
for i in range(	numStudents):
	# Tally the exam grades for the ith student.
	total = 0
	for j in range(numExams):
		total += examGrades[i, j]
		
	# Compute average for ith student.
	examAvg = float(total) / numExams
	print('%2d:	%6.2f' % (i+1, examAvg))
	