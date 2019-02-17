from Person import Person

# person is abstract class


class Student(Person):

    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


def main():

    s = Student("Shintu")

    print(s.getName())


if __name__ == "__main__":
    main()
