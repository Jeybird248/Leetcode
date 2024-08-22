# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        traversal = set()
        while headA:
            traversal.add(headA)
            headA = headA.next
        while headB:
            if headB in traversal:
                return headB
            else:
                headB = headB.next
        return None