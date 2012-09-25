"""
Project Euler script #4.
"""


def is_palindrome(n):
	string = str(n)
	if (string == string[::-1]):
		return True;
	return False

def main():
	largest_palindrome = 0

	for i in range(100, 999):
		for j in range(100, 999):
			product = i * j
			print "%d * %d = %d" % (i, j, product)
			if (is_palindrome(product)):
				print "It's a palindrome!"
				if (product > largest_palindrome):
					largest_palindrome = product

	print "largest palindrome: %d" % (largest_palindrome)

if __name__ == "__main__":
    main()