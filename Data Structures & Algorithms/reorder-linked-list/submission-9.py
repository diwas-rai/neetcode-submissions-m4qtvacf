class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        rev = prev
        l1 = head
        while rev:
            rev_next, l1_next = rev.next, l1.next
            l1.next = rev
            rev.next = l1_next
            l1 = l1_next
            rev = rev_next