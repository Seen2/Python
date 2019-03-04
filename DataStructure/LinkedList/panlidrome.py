from linkedList import LinkedList


def isPanildrome(li):
    ptr = li
    l = []
    while ptr != None:
        l.append(ptr.data)
        ptr = ptr.next

    if l == l[-1:-(len(l)+1):-1]:
        del l,  ptr
        return True
    else:
        del l,  ptr
        return False


def main():
    l = LinkedList(3)
    l.insert(5)
    l.insert(3)
    # l.insert(5)
    # l.insert(10)
    # l.insert(2)
    # l.insert(1)
    l.display()
    print(isPanildrome(l))


if __name__ == "__main__":
    main()
