from binarySearchTree import BinarySearchTree, Node

tree = BinarySearchTree()

tree.insert(tree.root, Node(34))

tree.insert(tree.root, Node(32))
tree.insert(tree.root, Node(39))

tree.insert(tree.root, Node(30))

print(tree.search(tree.root, 32))
print(tree.search(tree.root, 34))
print(tree.search(tree.root, 30))
print(tree.search(tree.root, 39))
