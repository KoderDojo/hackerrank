"""
 Insert Node at a specific position in a linked list
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

    def __repr__(self):
        return f'Node({self.data}, {self.next})'


# This is a "method-only" submission.
# You only need to complete this method.
def InsertNth(head, data, position):
    """
    >>> head = InsertNth(None, 5, 0)
    >>> assert(head.data == 5)
    >>> node = Node(1)
    >>> head = InsertNth(node, 5, 0)
    >>> assert(head.data == 5)
    >>> assert(head.next.data == 1)
    >>> node = Node(1)
    >>> head = InsertNth(node, 5, 1)
    >>> assert(head.data == 1)
    >>> assert(head.next.data == 5)
    >>> node = Node(1, Node(2))
    >>> head = InsertNth(node, 5, 2)
    >>> assert(head.data == 1)
    >>> assert(head.next.data == 2)
    >>> assert(head.next.next.data == 5)

    """
    if position == 0:
        return Node(data, head)

    current_node = head

    for _ in range(2, position + 1):
        current_node = current_node.next

    new_node = Node(data)

    if current_node.next is not None:
        new_node.next = current_node.next

    current_node.next = new_node

    return head
