# Implement binary search of a sorted array of integers
# returns position of searched for element

import sys

def recursive_binary_search(array, low, high, x):
	if high >= low:

		middle = low + (high - low)/2

		if array[middle] == x:
			return middle

		elif array[middle] > x:
			return recursive_binary_search(array, low, middle-1, x)

		else:
			return recursive_binary_search(array, middle+1, high, x)

	else:
		return -1

def binary_search(array, low, high, x):
	while low <= high:

		middle = low + (high - low)/2

		if array[middle] == x:
			return middle

		elif array[middle] > x:
			high = middle - 1

		else:
			low = middle + 1

	return -1

def main():
	line = sys.stdin.readline()
	array = list(map(int, line.split()))
	print array
	x = int(sys.stdin.readline())
	print x

	low = 0
	high = len(array) - 1

	print low, high

	result = recursive_binary_search(array, low, high, x)

	print result

	result = binary_search(array, low, high, x)

	print result


	return

if __name__ == "__main__":
    main()
