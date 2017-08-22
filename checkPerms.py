# Given two strings, determine if one is a permutation of the others.

import sys

def checkPermutations(a, b):
	hashA = {}
	hashB = {}

	if len(a) is not len(b):
		return False

	for char in a:
		if hashA.get(char, None) is not None:
			hashA[char] += 1
		else:
			hashA[char] = 1

	for char in b:
		if hashB.get(char, None) is not None:
			hashB[char] += 1
		else:
			hashB[char] = 1

	for x in hashA.keys():
		if hashA[x] != hashB[x]:
			return False

	return True

def main():
	a = sys.stdin.readline()
	b = sys.stdin.readline()

	print checkPermutations(a, b)

	return

if __name__ == "__main__":
    main()
