# Count the number of occurrences of each letter in a text file.

from my_own_array import Array

# Create an array for the counters and initialize each element to 0.
theCounters = Array(127)
theCounters.clear(0)

# Open the text file for reading and extract each line from the file
# and iterate over each character in the line.
with open('atextfile.txt', 'r') as theFile:
	content = theFile.read()
for letter in content:
	code = ord(letter)
	theCounters[code] += 1

# Print the result. The uppercase letters have ASCII values in the 
# range 65...90 and the lowercase letters are in the range 97...122.
for i in range(26):
	print('%c - %4d			%c - %4d' % \
		(chr(65+i), theCounters[65+i], chr(97+i), theCounters[97+i]))