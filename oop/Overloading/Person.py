class Person:
    def __init__(self, name="Unknown", age=0):
        assert type(age) == int
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

    def setIntro(self, name, age):
        assert type(age) == int
        self.name = name
        self.age = age

    def getIntro(self):

        intro = "This is " + self.name + " and I'm " + self.age + " years old."
        return intro
