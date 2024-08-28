# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or has only one node
        if not head or not head.next:
            return head

        # Step 1: Find the middle of the list
        mid = self.getMiddle(head)

        # Step 2: Split the list into two halves
        left = head
        right = mid.next
        mid.next = None  # Split the list

        # Step 3: Recursively sort each half
        left = self.sortList(left)
        right = self.sortList(right)

        # Step 4: Merge the two sorted halves
        return self.mergeTwoLists(left, right)

    def getMiddle(self, head: ListNode) -> ListNode:
        # Fast and slow pointer technique to find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to form the merged list
        dummy = ListNode(0)
        tail = dummy

        # Merge two sorted lists
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Append any remaining nodes
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next