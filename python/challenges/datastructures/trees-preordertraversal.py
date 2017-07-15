"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preOrder(root):
    if root is None:
        return

    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)


root = Node(3, Node(5, Node(1), Node(4)), Node(2, Node(6)))
preOrder(root)
# 3 5 1 4 2 6
