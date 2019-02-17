from Person import Person


class Student(Person):

    def __init__(self, name, age, college):
        super().__init__(name, age)
        self.college = college

# overriding getName() method

    def getName(self):
        return "This is " + self.name

    def setNameAndAge(self, name, age):
        Person.setName(self, name)  # we can also use super().setName(name)
        self.age = age
        pass


def main():

    s = Student("Shintu", 25, "JISCE")

    print(s.getName())

    s.setNameAndAge("Lokpati", 20)
    print(s.getName())

    # there are many method for operator for each new class we create
    # we can view them by way below

    print(dir(s))


if __name__ == "__main__":
    main()
