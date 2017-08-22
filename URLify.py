# URLify a string, ie replace spaces with %20

import sys

def URLify(input, length):
	numSpaces = 0

	for i in range(0, length):
		if input[i] == " ":
			numSpaces += 1

	x = length - 1

	for i in range(0, numSpaces):
		shift = 2*(numSpaces - i)
		while input[x] != " ":
			input[x+shift] = input[x]
			x -= 1

		shift = 2 * (numSpaces - (i + 1))
		input[x + shift] = '%'
		input[x + 1 + shift] = "2"
		input[x + 2 + shift] = "0"
		x -= 1

	return input

def main():
	a = list(sys.stdin.readline())
	length = int(sys.stdin.readline())
	
	print URLify(a, length)

	return

if __name__ == "__main__":
    main()
