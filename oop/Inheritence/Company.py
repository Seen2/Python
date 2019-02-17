class Company:

    def __init__(self, company):
        self.__company = company  # __company is private variable

    def setCompany(self, value):
        self.__company = value

    def getCompany(self):
        return self.__company
