"""
Project Euler problem #15.
"""
import math

def main():
	grid_side = 20

	# This one is easy, we need to find Rs (moves right) and Ds (move down)
	# All paths in a square grid will be size 2n, with equal numbers Rs and Ds
	# So it's just a binomial coefficient of 2 things, R and D
	# That's (2n)! / (n! * n!)
	paths = math.factorial(2 * grid_side) / (math.factorial(grid_side) * math.factorial(grid_side))
	print paths

if __name__ == "__main__":
    main()