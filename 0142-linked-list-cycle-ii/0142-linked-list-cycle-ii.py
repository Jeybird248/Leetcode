# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        length = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            length += 1
            if fast == slow:
                break
        if not length or (not fast or (fast and not fast.next)):
            return None
        
        
        fast1 = slow1 = head
        for i in range(length):
            fast1 = fast1.next
        while fast1 != slow1:
            fast1 = fast1.next
            slow1 = slow1.next
        return slow1