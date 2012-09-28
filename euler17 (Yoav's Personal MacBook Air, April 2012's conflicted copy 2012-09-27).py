"""
Project Euler problem #17.
"""

# From http://stackoverflow.com/questions/5620571/project-euler-problem-17-python
# A much more efficient approach: dictionaries with letter counts for the common words
# For example 1:3 for "one" having 3 letters
sd = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
dd1 = {10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:9,19:8}
dd2 = {2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
td = {0: 10, 1: 13, 2: 13, 3: 15, 4: 14, 5: 14, 6: 13, 7: 15, 8: 15, 9: 14}
cd = {0:0,1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:9,19:8}

def count_letters(number):
	""" Count words in the given number. """
	if number < 10:
		return sd[number % 10] # Direct dictionary lookup
	elif number < 100:
		if number < 20:
			return(dd1[number]) # Direct dictionary lookup
		else:
			return(dd2[number / 10] + sd[number % 10])  # If the number is > 20 do a construction 
	elif number < 1000:
		if number % 100 == 0:
			return sd[number / 100] + 7        # If the number is multiples of 100 give assuming single digit and 7 for hundred 
		elif number % 100 < 20:
			return td[number / 100] + cd[number % 100]  # If 3 digit numbers not more than *20 , then direct mapping 
	else:
		return td[number / 100] + dd2[(number % 100) / 10] + sd[number % 10]

def main():
	count = 0 
	for i in range(1, 1000):
		count = count + count_letters(i)
	print count + 11

if __name__ == "__main__":
    main()