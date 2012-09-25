"""
Project Euler script #2.
"""

fibs = {}

def fib(n):
	if n in fibs:
		return fibs[n]
			
	if (n < 2):
		fibs[n] = 1
	else:
		fibs[n] = fib(n-1) + fib(n-2)

	return fibs[n]

def main():
	sum = 0
	for i in range(1, 34):
		n = fib(i)
		if (n % 2 == 0):
			sum += n

	print sum

if __name__ == "__main__":
    main()