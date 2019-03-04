class BinarySearchTree:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

    def insert(self, val):
        return self.__insertVal(val, self)

    def __insertVal(self, val, node):

        if node == None:
            node = BinarySearchTree(val)
            node.data = val
            node.right = None
            node.left = None
            return True
        elif val > node.data:
            print(node.data)
            return self.__insertVal(val, node.right)
        elif val < node.data:
            print(node.data)
            return self.__insertVal(val, node.left)
        else:
            return False
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.right = None
#         self.left = None
