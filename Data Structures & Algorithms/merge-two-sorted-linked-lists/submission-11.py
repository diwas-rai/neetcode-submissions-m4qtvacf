# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        dummy = curr = ListNode()

        while l1 and l2:
            l1_val = l1.val
            l2_val = l2.val

            if l1_val >= l2_val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            
            curr = curr.next

        curr.next = l1 or l2

        return dummy.next
