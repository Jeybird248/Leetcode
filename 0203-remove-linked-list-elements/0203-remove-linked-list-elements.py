# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            if curr.val == val:
                if curr.val == head.val:
                    curr = curr.next
                    head = curr
                    continue
                else:
                    prev.next = curr.next
                    curr = curr.next
                    continue
                    
            prev = curr
            curr = curr.next
        
        return head