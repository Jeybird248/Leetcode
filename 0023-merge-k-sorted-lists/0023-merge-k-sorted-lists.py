# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        dummy = ListNode(0)
        curr = dummy
        while lists:
            minIdx = -1
            minVal = float("inf")
            interrupted = False
            for idx, l in enumerate(lists):
                if not l:
                    lists.pop(idx)
                    interrupted = True
                    break
                if l.val < minVal:
                    minIdx = idx
                    minVal = l.val
            if not interrupted:
                curr.next = lists[minIdx]
                curr = curr.next
                lists[minIdx] = lists[minIdx].next
        
        return dummy.next