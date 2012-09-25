"""
Project Euler problem #12.
"""

divisor_threshold = 500

def triangle(n):
	return sum(xrange(n))

def count_divisors(n):
	count = 0
	for i in range(1, n + 1):
		if n % i == 0:
			count += 1
	print "%d has %d divisors" % (n, count)
	return count

def main():
	i = 0
	max_divisors = 0
	max_divisors_i = 0
	while (max_divisors < divisor_threshold):
		divisors = count_divisors(triangle(i))
		if (divisors > max_divisors):
			max_divisors = divisors
			max_divisors_i = i
		if i % 10 == 0:
			print "Testing %d, max divisors so far: %d (for %d)" % (i, max_divisors, max_divisors_i)
		i += 1
	print "Found %d divisors for %d" % (max_divisors_i, max_divisors)

if __name__ == "__main__":
    main()