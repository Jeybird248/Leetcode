# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(start, end):
            curr = start
            prev = None
            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        length = 0
        curr2 = head
        while curr2:
            curr2 = curr2.next
            length += 1
            
        for i in range(length // k):
            start = end = curr.next
            for i in range(k):
                end = end.next
            prev_head = reverse(start, end)

            curr.next = prev_head
            start.next = end
            
            curr = start
            
        return dummy.next