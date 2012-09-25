"""
Project Euler problem #10.
"""
import math

# Global: max number we're looking for
limit = 2000000

# Global: primes found
primes = []

# Global: list of booleans, initially all true
numbers = []

def is_prime(n):
	""" Figure out if the given number is a prime. """
	for prime in primes:
		if(n % prime == 0):
			return False
	return True

def mark_primes(n):
	""" Go over the numbers from 1 to limit looking for primes. """
	x = 2
  	while(x*n < limit):
  		if(numbers[x*n]):
  			numbers[x*n] = False
  		x += 1

def main():
	""" Entry point. """

	# Initially set everything to true
	for x in xrange(0, limit):
		numbers.append(True)
 
	numbers[0] = False
	numbers[1] = False
 
	# start with multiples of primes from 2 to ceil(sqrt(limit))
	for x in xrange(2, int(math.ceil(math.sqrt(limit)))):
 		# if prime, add to prime pool and mark it and it's multiples
 		if(is_prime(x)):
 			print "Found prime: %d" % x
 			primes.append(x)
			mark_primes(x)

	# calculate the final sum
	total = 0
 	for x in xrange(0, len(numbers)):
		if(numbers[x]):
			total += x

	print "Total: %d " % total

if __name__ == "__main__":
    main()