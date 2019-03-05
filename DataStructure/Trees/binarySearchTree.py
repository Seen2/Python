class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, node):
        '''
        root=binary tree root.
        node is of type Node.
        node.data=val,node.left=None,node.right=None.

        '''
        assert type(node) == Node
        if root == None:
            self.root = node
            return True
        elif root.data > node.data:
            # print(root.data)
            if root.left == None:
                root.left = node
                return True
            else:
                return self.insert(root.left, node)
        elif root.data < node.data:
            # print(root.data)
            if root.right == None:
                root.right = node
                return True
            else:
                return self.insert(root.right, node)
        else:
            return False

    def search(self, root, val):
        '''
        root=binary tree root.

        '''
        if root.data == val:
            return True
        elif root.data > val:
            return self.search(root.left, val)
        elif root.data < val:
            return self.search(root.right, val)
        else:
            return False
