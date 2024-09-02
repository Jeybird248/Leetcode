# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has one element, it's already sorted
        if not head or not head.next:
            return head
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split the list into two halves
        middle = slow.next
        slow.next = None
        
        # Step 3: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(middle)
        
        # Step 4: Merge the two sorted halves
        dummy = ListNode(0)
        current = dummy
        
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        
        # Append the remaining nodes from left or right
        if left:
            current.next = left
        if right:
            current.next = right
        
        return dummy.next
