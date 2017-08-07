# Find the first X prime numbers

import sys

def main():
	x = int(sys.stdin.readline())

	primes = []
	if x >= 2:
		primes.append(2)

	for i in range(3, x+1):
		is_prime = True

		for j in range(0, len(primes)):
			if i % primes[j] == 0:
				is_prime = False
				break

		if is_prime:
			primes.append(i)

	print primes

	return

if __name__ == "__main__":
    main()
