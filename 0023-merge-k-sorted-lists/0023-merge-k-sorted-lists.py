# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        
        while any(l is not None for l in lists):
            minVal, minNode, minIdx = float("inf"), None, -1
            for idx, l in enumerate(lists):
                if l and l.val < minVal:
                    minVal = l.val
                    minIdx = idx
            
            if minIdx != -1:
                curr.next = lists[minIdx]
                curr = curr.next
                lists[minIdx] = lists[minIdx].next        

        return dummy.next