"""
Project Euler problem #14.
"""

def next(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3 * n + 1

def chain(n):
	numbers = [n]
	n2 = next(n)
	while (n2 > 1):
		numbers.append(n2)
		n2 = next(n2)
	numbers.append(1) # for completeness 

	#print "chain(%d) = %s" % (n, numbers)
	return numbers

def main():
	max_length = 0
	max_length_i = 0
	limit = 1000000
	for i in range(1, limit):
		if i % 100000 == 0:
			print "Testing %d" % i
		length = len(chain(i))
		if length > max_length:
			max_length = length
			max_length_i = i

	print "%d has the longest chain, at %d terms." % (max_length_i, max_length)

if __name__ == "__main__":
    main()