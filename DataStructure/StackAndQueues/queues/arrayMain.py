from arrayQueue import Queue


def main():
    q = Queue(10)
    q.enqueue(1)
    q.enqueue(2)
    q.display()
    print(q.peek())
    q.dequeue()
    print("after deque")
    q.display()
    print(q.isEmpty())
    print(q.peek())


if __name__ == "__main__":
    main()
