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
        
        dummy = ListNode(0)
        
        dummy.next = head
        curr = dummy
        
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
            
        while length >= k:
            start = curr.next
            end = start
            for i in range(k):
                end = end.next
            
            # Reverse the k-group
            reversed_head = reverse(start, end)
            
            # Connect reversed part to the previous section
            curr.next = reversed_head
            start.next = end
            
            # Move the pointers to the next section
            curr = start
            
            # Reduce the length by k
            length -= k
            
        return dummy.next