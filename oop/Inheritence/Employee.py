from Person import Person
from Company import Company


class Employee(Person, Company):

    def __init__(self, name, company):
        Person.__init__(self, name)
        Company.__init__(self, company)


def main():

    e = Employee("Tony Stark", "Stark Industry")

    print(e.getCompany())
    e.name = "Shintu"
    print(e.name)
    e.__company = "tiwari"  # can't set private variable
    print(e.getCompany())
    e.setCompany("Tiwari")
    print(e.getCompany())


if __name__ == "__main__":
    main()
