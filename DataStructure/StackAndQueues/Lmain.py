from linkedListStack import Stack


def main():
    s = Stack(10)
    print(s.push(10))
    s.push(11)
    s.display()
    s.pop()
    print("after pop")

    s.display()

    print(s.isEmpty())

    print(s.peek())


if __name__ == "__main__":
    main()
