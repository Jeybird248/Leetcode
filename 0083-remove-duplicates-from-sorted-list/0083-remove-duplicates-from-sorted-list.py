# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        curr = head
        appeared = set()
        while curr:
            if curr.val not in appeared:
                appeared.add(curr.val)
                if prev:
                    prev.next = curr
                    curr = curr.next
                    prev = prev.next
                else:
                    prev = curr
                    curr = curr.next
            else:
                if not curr.next:
                    prev.next = None
                curr = curr.next
                
        return head