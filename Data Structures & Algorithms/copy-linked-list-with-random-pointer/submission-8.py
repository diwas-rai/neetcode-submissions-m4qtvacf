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
        old_to_new = {}

        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        for old in old_to_new.keys():
            old_to_new[old].next = old_to_new[old.next] if old.next else None
            old_to_new[old].random = old_to_new[old.random] if old.random else None
        
        return old_to_new[head] if head else None