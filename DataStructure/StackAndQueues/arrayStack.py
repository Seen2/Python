class Stack:
    def __init__(self, capacity):
        self.__data = [0]*capacity
        self.__capacity = capacity
        self.__top = 0

    def push(self, val):
        if self.__capacity >= self.__top+1:
            self.__data[self.__top] = val
            self.__top += 1
            return True
        else:
            print("Stack Overflow")
            return False

    def pop(self):
        if self.__top > 0:
            self.__data[self.__top] = 0
            self.__top -= 1
            return True
        else:
            print("Stack is empty")
            return False

    def display(self):
        for i in range(self.__top-1, -1, -1):
            print(self.__data[i])

    def isEmpty(self):
        if self.__top == 0:
            return True
        else:
            return False

    def peek(self):
        return self.__data[self.__top]


def main():
    pass


if __name__ == "__main__":
    main()
