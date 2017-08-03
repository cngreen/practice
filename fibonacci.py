# Write fibonacci iteratively and recursively

import sys

def iter_fibo(n):
	x, y = 0, 1

	for i in range(0, n):
		x, y = y, x + y

	return x

def recurs_fibo(n):
	if n <= 1:
		return n

	return (recurs_fibo(n-1) + recurs_fibo(n-2))

def main():
	n = int(sys.stdin.readline())

	print iter_fibo(n)

	print recurs_fibo(n)

	return

if __name__ == "__main__":
    main()