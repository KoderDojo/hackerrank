"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while len(queue) > 0:
        node = queue.popleft()

        print(node.data, end=' ')

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

root = Node(3, Node(5, Node(1), Node(4)), Node(2, Node(6)))
level_order(root)
# 3 5 2 1 4 6
