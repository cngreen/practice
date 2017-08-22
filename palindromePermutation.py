# given a string, determine if it is a permutation of a palindrome.

import sys

def permPal(input):
	CHARS = {}

	print input

	for char in input:
		if CHARS.get(char, None) is not None:
			CHARS[char] += 1
		else:
			CHARS[char] = 1

	oddChar = 0

	for char in CHARS.keys():
		if CHARS[char]%2 is not 0:
			print char
			print CHARS[char]
			oddChar += 1
			if oddChar > 1:
				return False

	return True
	

def main():
	a = sys.stdin.readline()
	a = a.strip()
	
	print permPal(a)

	return

if __name__ == "__main__":
    main()
