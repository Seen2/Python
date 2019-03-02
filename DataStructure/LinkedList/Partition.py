from linkedList import LinkedList


def partition(l, x):
    ptr = l
    lt = []
    gt = []
    while ptr != None:
        if ptr.data >= x:
            gt.append(ptr.data)
        else:
            lt.append(ptr.data)
        ptr = ptr.next
    l = lt+gt
    lList = LinkedList(l[0])
    n = len(l)
    del gt, lt, ptr
    for i in range(1, n):
        lList.insert(l[i])
    del l, n
    return lList


def main():
    l = LinkedList(3)
    l.insert(5)
    l.insert(8)
    l.insert(5)
    l.insert(10)
    l.insert(2)
    l.insert(1)
    l.display()
    l = partition(l, 5)
    print("next")
    l.display()


if __name__ == "__main__":
    main()
