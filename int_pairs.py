# Find pairs in an integer array whose sum is equal to k
# expected no duplicate integers

import sys

def main():
	k = int(sys.stdin.readline())
	print k

	line = sys.stdin.readline()
	array = list(map(int, line.split()))
	print array

	my_dict = {}
	for i in range(0, len(array)):
		my_dict[array[i]] = i

	for key in my_dict.keys():
		if (k-key) > key: #avoid duplicates
			if (k - key) in my_dict.keys() and my_dict[key] != my_dict[k-key]:
				print key, (k-key)

	return

if __name__ == "__main__":
    main()