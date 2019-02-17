from time import sleep


def main():
    n = int(input("Enter iteration "))
    print("For loop")
    for i in range(n):
        print(f"{i}")

    sleep(1)

    print("While loop")
    while n is not -1:
        print(f"{n}")
        n -= 1


if __name__ == '__main__':
    main()
