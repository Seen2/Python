class Person:
    def __init__(self, name="Unknown", age=0):
        assert type(age) == int
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


def main():
    p = Person()
    print(p.name)


if __name__ == "__main__":
    main()
