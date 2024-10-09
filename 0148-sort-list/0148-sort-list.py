# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        temp = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(temp)
        
        dummy = ListNode()
        curr = dummy
        
        while left and right:
            if left.val > right.val:
                curr.next = right
                curr = curr.next
                right = right.next
            else:
                curr.next = left
                curr = curr.next
                left = left.next
        if left:
            curr.next = left
        if right:
            curr.next = right
        
        return dummy.next
