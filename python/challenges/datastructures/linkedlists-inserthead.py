"""
 Insert Node at the begining of a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Insert(head, data):
    """
    >>> head = None
    >>> node = Insert(head, 5)
    >>> assert(node.data == 5)
    >>> head = Node(7)
    >>> node = Insert(head, 5)
    >>> assert(node.data == 5)
    >>> assert(node.next.data == 7)
    """
    first_node = Node(data)

    if head is None:
        return first_node

    first_node.next = head

    return first_node
