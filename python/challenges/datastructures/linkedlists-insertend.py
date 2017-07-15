"""
 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Insert(head, data):
    """
    >>> head = None
    >>> node = Insert(head, 4)
    >>> assert(node.data == 4)
    >>> head = Node(6)
    >>> node = Insert(head, 4)
    >>> assert(node.next.data == 4)
    >>> head = Node(6, Node(7))
    >>> node = Insert(head, 4)
    >>> assert(node.next.next.data == 4)
    """
    last_node = Node(data)

    if head is None:
        return last_node

    current_node = head

    while current_node.next is not None:
        current_node = current_node.next

    current_node.next = last_node

    return head
