class LinkedList:
    def __init__(self, val=0):
        self.data = val
        self.next = None
        self.tail = self

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
                temp = LinkedList(val)
                self.next = temp.tail
                temp.next = None
                break
            self = self.next

        # temp=LinkedList(val)

    # def insertAtHead(self, val):
    #     """
    #     insert val at Head of linked list.
    #     """
    #     first = LinkedList(val)
    #     first.next = self.next
    #     del self
    #     self = first
    #     self.display()
