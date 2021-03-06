# inorder traversal
# Algorithm Inorder(tree)
#    1. Traverse the left subtree, i.e., call Inorder(left-subtree)
#    2. Visit the root.
#    3. Traverse the right subtree, i.e., call Inorder(right-subtree)
# eg.
#                 a                           a
#              /     \                     /     \
#             b        c                  b       c
#           /   \        \                 \     /
#         d       e       f                 d    e
#       /   \           /   \                     \
#      g     h         i     j                      f
#             \             /                      /
#              l           k                      g
#                                               /   \
#                                              h     i
# inorder: g,d,h,l,b,e,a,c,i,f,k,j.
# inorder: b,d,a,e,h,g,i,f,c.

# Algorithm Preorder(tree)
#    1. Visit the root.
#    2. Traverse the left subtree, i.e., call Preorder(left-subtree)
#    3. Traverse the right subtree, i.e., call Preorder(right-subtree)
# eg.
#                 a                           a
#              /     \                     /     \
#             b        c                  b       c
#           /   \        \                 \     /
#         d       e       f                 d    e
#       /   \           /   \                     \
#      g     h         i     j                      f
#             \             /                      /
#              l           k                      g
#                                               /   \
#                                              h     i
# preorder: a,b,d,g,h,l,e,c,f,i,j,k.
# preorder: a,b,d,c,e,f,g,h,i.
#
#
#
# Algorithm Postorder(tree)
#    1. Traverse the left subtree, i.e., call Postorder(left-subtree)
#    2. Traverse the right subtree, i.e., call Postorder(right-subtree)
#    3. Visit the root.
# eg.
#                 a                           a
#              /     \                     /     \
#             b        c                  b       c
#           /   \        \                 \     /
#         d       e       f                 d    e
#       /   \           /   \                     \
#      g     h         i     j                      f
#             \             /                      /
#              l           k                      g
#                                               /   \
#                                              h     i
#
#
# postorder: g,l,h,d,e,b,i,k,j,f,c,a.
# postorder: d,b,h,i,g,f,e,c,a.
#
