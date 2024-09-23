# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        prev = None
        while curr and curr.next:
            if curr == head:
                temp = curr.next.next
                curr = head.next
                head.next = temp
                curr.next = head
                prev = head
                head = curr
                curr = prev.next
            else:
                temp = curr.next.next
                temp2 = curr
                curr = temp2.next
                temp2.next = temp
                prev.next = curr
                curr.next = temp2
                prev = temp2
                if prev:
                    curr = prev.next
        return head