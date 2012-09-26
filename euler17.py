"""
Project Euler problem #17.
"""

def words(number):
	if number == 1:
		return 'one'
	elif number == 2:
		return 'two'
	elif number == 3:
		return 'three'
	elif number == 4:
		return 'four'
	elif number == 5:
		return 'five'
	elif number == 6:
		return 'six'
	elif number == 7:
		return 'seven'
	elif number == 8:
		return 'eight'
	elif number == 9:
		return 'nine'
	elif number == 10:
		return 'ten'
	elif number == 11:
		return 'eleven'
	elif number == 12:
		return 'twelve'
	elif number == 13:
		return 'thirteen'
	elif number == 14:
		return 'fourteen'
	elif number == 15:
		return 'fifteen'
	elif number == 16:
		return 'sixteen'
	elif number == 17:
		return 'seventeen'
	elif number == 18:
		return 'eighteen'
	elif number == 19:
		return 'nineteen'
	else:
		return 'TBD'

def count_letters(number):
	return len(words(number))

def sum_letters(start, end):
	total = 0
	for number in range(start, end):
		total += count_letters(number)
	return total

def main():
	print "%d letters total." % sum_letters(1, 10)

if __name__ == "__main__":
    main()