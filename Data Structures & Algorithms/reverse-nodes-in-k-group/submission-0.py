# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        prevNode = dummy

        while True:
            kth = self.get_kth(prevNode,k)
            if not kth:
                break

            groupNext = kth.next

            prev,curr = kth.next,prevNode.next
            while curr!= groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = prevNode.next
            prevNode.next = kth
            prevNode = tmp

        return dummy.next

    def get_kth(self,node,k):
        while node and k>0:
            node = node.next
            k-=1
        return node