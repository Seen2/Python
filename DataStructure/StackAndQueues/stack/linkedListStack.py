from linkedList import LinkedList


class Stack:
    def __init__(self, capacity):
        self.__data = LinkedList()
        self.__capacity = capacity
        self.__top = 0

    def push(self, val):
        if self.__capacity >= self.__top+1:
            self.__data.insert(val)
            self.__top += 1
            return True
        else:
            print("Stack Overflow")
            return False

    def pop(self):
        if self.__top > 0:
            ptr = self.__data
            while True:
                if self.__top == 1:
                    self.__init__(self.__capacity)
                    break
                if ptr.next.next == None:
                    ptr.next = None
                    break
                ptr = ptr.next

            self.__top -= 1
            return True
        else:
            print("Stack is empty")
            return False

    def display(self):
        self.__data.display()

    def isEmpty(self):
        if self.__top == 0:
            return True
        else:
            return False

    def peek(self):
        ptr = self.__data
        while True:
            if ptr.next == None:
                return ptr.data
            ptr = ptr.next


def main():
    pass


if __name__ == "__main__":
    main()
