# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        first = head
        second = head.next
        secondDummy = second
        while second and second.next:
            first.next = first.next.next
            second.next = second.next.next
            first = first.next
            second = second.next
            
        first.next = secondDummy
        return head