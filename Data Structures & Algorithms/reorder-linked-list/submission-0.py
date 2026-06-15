class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow ,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        second = prev
        first = head
        while second:
            tmp1, tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            second = tmp2
            first = tmp1