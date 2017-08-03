# Given 2 integer arrays, determine of the 2nd array is a rotated version of the 1st array. 
# Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}
# assumes no repeat integers

import sys

def main():
	line = sys.stdin.readline()
	a1 = list(map(int, line.split()))
	print a1

	line = sys.stdin.readline()
	a2 = list(map(int, line.split()))
	print a2

	if len(a1) is not len(a2):
		print False
		return

	index = -1
	is_rot = False
	j = 0

	for i in range(0, len(a1)): # to work with repeats, could consider adding if !is_rot && index != -1, can update index; else can't update index
		if a1[i] == a2[0]:
			index = i

		if index is not -1:
			if a1[i] == a2[j]:
				is_rot = True
			else:
				is_rot = False
				break
			j += 1

	if is_rot:
		for i in range(0, index):
			if a1[i] is not a2[j]:
				is_rot = False
				break

			j += 1

	print is_rot


	return

if __name__ == "__main__":
    main()