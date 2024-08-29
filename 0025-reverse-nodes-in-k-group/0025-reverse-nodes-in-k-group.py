# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # problem breaks down to reversing linkedlist
        def reverse(start, end):
            prev = None
            curr = start
            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
                
        # Determine the length of the linked list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        # Dummy node to simplify the reversal logic
        dummy = ListNode(0)
        dummy.next = head
        prev_end = dummy
        
        while length >= k:
            start = prev_end.next
            end = start
            
            # Move the `end` pointer k steps ahead
            for _ in range(k):
                end = end.next
            
            # Reverse the segment
            prev_end.next = reverse(start, end)
            
            # Move `prev_end` k steps ahead to the new segment
            start.next = end
            prev_end = start
            
            length -= k
        
        return dummy.next