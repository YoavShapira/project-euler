"""
Project Euler script #9.
"""
import math

def main():
	limit = 1000
	for a in range(1, limit + 1):
		for b in range(1, limit + 1):
			c = 1000 - b - a
			if a * a + b * b == c * c:
				return a * b * c


if __name__ == "__main__":
    print main()