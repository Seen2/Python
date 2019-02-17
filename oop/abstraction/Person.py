from abc import ABC, abstractmethod

# person is abstract class


class Person(ABC):

    @abstractmethod
    def setName(self, value): pass

    @abstractmethod
    def getName(self): pass
