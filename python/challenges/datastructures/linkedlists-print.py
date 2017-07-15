"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 If head is None, print nothing.

 Input: 1->2->3->None
 Output:
   1
   2
   3
"""


def print_list(head):
    if head is None:
        return

    print(head.data)
    print_list(head.next)
