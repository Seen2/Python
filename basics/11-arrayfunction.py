# way to define global variable
__COUNT = 3


def main():
	x = []
	for i in range(__COUNT):
		d = int(input(f"Enter times to {i+1}-Score:"))
		x.append(d)
	plot(x)


def plot(n):
	for i in range(__COUNT):
		print(f"{i+1}-Score[{n[i]}]:");
		for j in range(n[i]):
			print("#", end="")
		print("")


if __name__ == '__main__':
	main()



