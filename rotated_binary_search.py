# Implement binary search of a rotated, sorted array of integers
# returns position of searched for element

import sys

def find_rotation_point(array, low, high):
	if high < low:
		return -1
	if high == low:
		return low

	middle = (low + high)/2

	if middle < high and array[middle] > array[middle+1]:
		return middle
	if middle > low and array[middle] < array[middle-1]:
		return (middle-1)

	if array[low] >= array[middle]:
		return find_rotation_point(array, low, middle-1)
	else:
		return find_rotation_point(array, middle+1, high)

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

	low = 0
	high = len(array) - 1

	rotation_point = find_rotation_point(array, low, high)

	if rotation_point == -1:
		result = binary_search(array, low, high, x)
		print result

		return

	else:
		if array[rotation_point] == x:
			print rotation_point
			return

		elif array[0] <= x:
			result = binary_search(array, low, rotation_point-1, x)
			print result
			return
		else:
			result = binary_search(array, rotation_point+1, high, x)
			print result
			return

	return

if __name__ == "__main__":
    main()
