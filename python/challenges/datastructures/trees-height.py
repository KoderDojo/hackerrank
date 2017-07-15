"""
Get Height of Binary Tree
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def get_height(root):
    """
    >>> assert(get_height(None) == -1)
    >>> root = Node(1)
    >>> assert(get_height(root) == 0)
    >>> root = Node(1, Node(2))
    >>> assert(get_height(root) == 1)
    >>> root = Node(1, Node(2, Node(3)))
    >>> assert(get_height(root) == 2)
    """

    if root is None:
        return -1

    height_left = get_height(root.left)
    height_right = get_height(root.right)

    return 1 + max(height_left, height_right)
