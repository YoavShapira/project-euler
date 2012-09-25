"""
Project Euler script #9.
"""
import math

def is_triplet(a, b, c):
	print "Testing %d, %d, %d" % (a, b, c)
	return a*a + b*b == c*c

def main():
	a = 1
	b = 2
	c = 3
	desired_triplet = []

	while (a+b+c <= 1000):
		if (is_triplet(a,b,c)):
			print "Triplet!!! %d, %d, %d" % (a, b, c)
			if (a + b + c == 1000):
				desired_triplet = [a, b, c]
		a += 1
		b += 1
		c += 1
	
	print "Done!  Desired triplet: %s" % Desired_triplet

if __name__ == "__main__":
    main()