# Find the only element in an array that only occurs once.

import sys

def main():
	line = sys.stdin.readline()
	array = list(map(int, line.split()))
	print array

	# determine k
	k = max(array) + 1

	# soltuion that doesn't modify array but memory of O(k)
	result = [0] * k

	for i in range(0, len(array)): # the index of the result array is the number of times the element occurs
		result[array[i]] += 1

	
	for i in range(0, len(result)):
		if result[i] == 1:
			number = i
			break

	print number

	# solution that requires a particular repetition pattern:
	# here using find the one with one repetition with everything else 3 times

	result = 0

	x = None
	sum = None

	for i in range(0, 8): # 8 bit INT
		sum = 0
		x = (1 << i)

		for j in range(0, len(array)):
			if array[j] & x:
				sum += 1

		if (sum % 3):
			result |= x

	print result

	return

if __name__ == "__main__":
    main()
