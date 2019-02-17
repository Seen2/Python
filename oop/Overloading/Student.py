from Person import Person


class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

# overriding

    def getIntro(self):
        intro = f"This is {self.name}  and I'm  {self.age} years old. I study {self.course}."
        return intro

# overloading

    def setIntro(self, name, age, course):
        assert type(age) == int
        self.name = name
        self.age = age
        self.course = course

# overloading

    def __str__(self):
        intro = f"This is {self.name}  and I'm  {self.age} years old. I study {self.course}."
        assert type(intro) == str
        return intro


def main():
    s = Student("Tony Stark", 102, "Robotics")
    # print(s.getIntro())
    # s.setIntro("Iron Man", 1000, "Saving world")
    # print(s.getIntro())
    print(str(s))


if __name__ == "__main__":
    main()
