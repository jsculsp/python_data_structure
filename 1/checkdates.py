# -*- coding:utf-8 -*-

# Extracts a collection of birth dates from the user
# and determines if each individual is at least 21 years of age.

from datetime import date
from linearbag import Bag

# Prompts for and extracts the Gregorian date components.
# Returns a date object or None when the user has finished entering dates.
def promptAndExtractDate():
	print('Enter a birth date.')
	year = input('year (0 to quit): ')
	if year == 0:
		return None
	else:
		month = input('month: ')
		day = input('day: ')
		return date(year, month, day)
		
def main():
		# Date before which a person must have been born to be 21 or older.
		bornBefore = date(1995, 06, 27)
		bag = Bag()
		
		# Extract birth dates from the user and determine if 21 or older.
		date_input = promptAndExtractDate()
		while date_input is not None:
			bag.add(date_input)
			date_input = promptAndExtractDate()
			
		# Iterate over the bag and check the age.
		for date1 in bag:
			if date1 <= bornbefore :
				print('Is at least 21 years of age: ', date1)
			
if __name__ == '__main__':
	main()