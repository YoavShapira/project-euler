"""
Project Euler problem #15.
"""
import math

def main():
	number = 2 ** 1000
	digits = list(str(number))
	print sum([int(i) for i in digits])

if __name__ == "__main__":
    main()