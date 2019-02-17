from Person import Person


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)

        self.course = course


def main():

    s = Student("Tony Stark", "Robotics")

    print(s.course)


if __name__ == "__main__":
    main()
