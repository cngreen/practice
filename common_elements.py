# Find the common elements of 2 int arrays

import sys

def main():
	line = sys.stdin.readline()
	array1 = list(map(int, line.split()))
	print array1
	line = sys.stdin.readline()
	array2 = list(map(int, line.split()))
	print array2

	# determine k
	k = max(array1) + 1

	if (max(array2) + 1) > k:
		k = max(array2) + 1

	# O(2n) solution that doesn't modify array but memory of O(2k)
	# ignores duplicates
	result1 = [False] * k
	result2 = [False] * k

	for i in range(0, len(array1)): # the index of the result array is the number of times the element occurs
		result1[array1[i]] = True

	for i in range(0, len(array2)):
		result2[array2[i]] = True

	
	for i in range(0, len(result1)):
		if result1[i] and result2[i]:
			print i

	# with sorted arrays:
	# this doesn't ignore duplicates

	array1.sort()
	array2.sort()

	i = 0
	j = 0
	while i < len(array1) and j < len(array2):
		if array1[i] == array2[j]:
			print array1[i]
			i += 1
			j += 1
		elif array1[i] < array2[j]:
			i += 1
		else:
			j += 1


	return

if __name__ == "__main__":
    main()
