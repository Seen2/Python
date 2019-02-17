class Person:

    def __init__(self, name):
        self.name = name


def main():
    p = Person("Tony Stark")
    print("Hello, ", end="")
    print(p.name)


if __name__ == "__main__":
    main()

