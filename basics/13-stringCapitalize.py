def main():
	s = input("Enter your name:")
	for c in s:

		if ord(c) in range(97, 97+25):
			print(chr(ord(c)-32), end="")
		else:
			print(c, end="")
	print()


if __name__ == '__main__':
	main()



