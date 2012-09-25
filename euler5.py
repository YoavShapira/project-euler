"""
Project Euler script #5.
"""

def div_11_to_20(divided):
	return all([not bool(divided % x) for x in xrange(11,20+1)])

def main():
	count = 2520
	while div_11_to_20(count) == False:
		count += 2520
 
  	print "%s" % count

if __name__ == "__main__":
    main()