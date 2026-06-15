# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slo ,fas = head, head

        while fas and fas.next:
            slo = slo.next
            fas = fas.next.next
            if slo == fas:
                return True
        return False