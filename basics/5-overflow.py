from time import sleep


def main():
	i = 2
	while True:
		print(f"{i}")
		i *= i
	sleep(1)


if __name__ == '__main__':
	main()

