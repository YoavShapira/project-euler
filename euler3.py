"""
Project Euler problem #3.
"""
import math

def primes(n):
    """ This is from http://code.activestate.com/recipes/366178/ """
    if n == 2: return [2]
    elif n < 2: return []

    s = range(3, n + 1, 2)
    mroot = n ** 0.5
    half = (n + 1) / 2 - 1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3) / 2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3

    return [2]+[x for x in s if x]

def main():
	target = 600851475143

	primes_to_check = primes(int(math.ceil(math.sqrt(target))))
	print "Got %d primes to check" % len(primes_to_check)

	prime_factors = []
	for number in primes_to_check:
		s = 1
		while s == 1:
			if target % number == 0:
				prime_factors.append(number)
				target /= number
			else:
				s = 0

	print "All done, prime_factors: %s" % prime_factors

if __name__ == "__main__":
	main()