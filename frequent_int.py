# Find the most frequent integer in an array
# the array contains numbers in range from 0 to k-1 where k is a positive integer and k <= n.

import sys

def main():
	line = sys.stdin.readline()
	array = list(map(int, line.split()))
	print array

	# determine k
	k = max(array) + 1
	print k

	# soltuion that doesn't modify array but memory of O(k)
	result = [0] * k

	for i in range(0, len(array)): # the index of the result array is the number of times the element occurs
		result[array[i]] += 1

	freq = result[0]
	number = 0
	
	for i in range(0, len(result)):
		if result[i] > freq:
			freq = result[i]
			number = i

	print number

	# solution that doesn't modifies array but memory of O(1)
	for i in range(0, len(array)):
		array[array[i]%k] += 2*k # using the mod operator and incrementing by a multiple of k ensures that we get the correct index

	freq = array[0]
	number = 0
	
	for i in range(0, len(result)):
		if array[i] > freq:
			freq = array[i]
			number = i

	print number

	return

if __name__ == "__main__":
    main()