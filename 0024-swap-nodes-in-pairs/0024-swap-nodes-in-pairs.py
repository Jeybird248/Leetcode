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
        while curr and curr.next:
            if curr == head:
                temp = head.next
                curr.next = temp.next
                temp.next = curr
                head = temp
            else:
                prev = curr
                curr = curr.next
                temp = curr
                if curr.next:
                    curr = curr.next
                    temp.next = curr.next
                    curr.next = temp
                prev.next = curr
                curr = curr.next
                
            
        return head