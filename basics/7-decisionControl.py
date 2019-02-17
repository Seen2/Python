from sys import exit


def main():
	x = int(input("Enter x:"))
	y = int(input("Enter y:"))

	if x < y:
		while True:
			x += 1
			if x > y:
				if x > y:
					print("x is equal to y")
					print(f"x={x}")

					# continue
					exit(0)
				break

	elif x > y:
		while True:
			x -= 1
			if x < y:
				print("x is equal to y")
				print(f"x={x}")
				break

	else:
		pass


if __name__ == '__main__':
	main()



