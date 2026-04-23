"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None:None}

        # iterate through the linkedlist and copy each old node, hashing the old node to a value of new node
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # iterate through the dict and add the pointers for each new node
        curr = head
        while curr:
            new = old_to_new[curr]
            new.next = old_to_new[curr.next]
            new.random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]