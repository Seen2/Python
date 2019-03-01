class LinkedList:
    def __init__(self, val=None, next=None):
        self.data = val
        self.next = next

    def display(self):
        """
          show wntire of linked list.
        """
        ptr = self
        while True:
            print(ptr.data)

            if ptr.next == None:
                break
            ptr = ptr.next

        del ptr

    def insert(self, val):
        """
        insert val at end of linked list.
        """
        self
        while True:
            if self.next == None:
                self.next = LinkedList(val)
                break
            self = self.next

    def deleteDups(self):
        s = []
        ptr = self
        while True:
            if ptr == self:
                s.append(ptr.data)
            if ptr.next == None:
                break
            if ptr.next.data in s:
                ptr.next = ptr.next.next
                if ptr.next == None:
                    break
            else:
                s.append(ptr.next.data)
                ptr = ptr.next

        print(s)

    def delete(self, val):
        ptr = self
        while True:
            if ptr.next == None:
                if ptr.data == val:
                    self = LinkedList()
                    return True
                else:
                    return False
            elif ptr.next.data == val:
                ptr.next = ptr.next.next
                return True
            elif ptr.data == val:
                self.__init__(self.next.data, self.next.next)

                return True
            else:
                ptr = ptr.next
        return False

    def deleteKthFromLast(self, k=0):
        tb = []
        ptr = self
        while True:
            if ptr.next == None:
                if k == 1:
                    self.__init__()
                    return True

                return False
            elif len(tb) == k:
                if ptr.next.next != None:
                    tb.reverse()
                    tb.pop()
                    tb.reverse()
                    ptr = ptr.next
                else:
                    if tb[0].next != None:
                        tb[0].next = tb[0].next.next

                    else:
                        tb[0] = None
                    return True

            else:
                ptr = ptr.next
            tb.append(ptr.next)
        return False


# temp = LinkedList(val)


def insertAtHead(self, val):
    pass

    # """
    # insert val at Head of linked list.
    # """
    # first = LinkedList(val)
    # first.next = self.next
    # del self
    # self = first
    # self.display()
