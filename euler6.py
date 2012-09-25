"""
Project Euler script #6.
"""

def main():
	sum_s = 0
	square_s = 0
	for i in range(1, 101):
		sum_s += (i * i)
		square_s += i
		print i
	print (square_s * square_s) - sum_s


if __name__ == "__main__":
    main()