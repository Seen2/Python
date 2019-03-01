from linkedList import LinkedList

# from linkedList1 import LinkedList


def main():
    l = LinkedList(9)
    l.insert(10)
    l.insert(9)
    l.insert(11)
    l.insert(11)
    # l.deleteDups()
    # print("\n")
    # print(l.delete(11))
    l.display()
    print(l.deleteKthFromLast(1))
    print("\n")
    try:
        l.display()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
