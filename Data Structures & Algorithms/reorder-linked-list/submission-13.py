# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        h2 = slow.next
        prev = slow.next = None

        while h2:
            temp = h2.next
            h2.next = prev
            prev = h2
            h2 = temp
        
        h1 = head
        h2 = prev

        while h2:
            h1_nxt, h2_nxt = h1.next, h2.next
            h1.next = h2
            h1 = h1_nxt
            h2.next = h1
            h2 = h2_nxt
        