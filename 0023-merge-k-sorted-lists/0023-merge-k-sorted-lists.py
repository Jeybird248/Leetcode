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
        while len(lists) > 1:
            currMin = float("inf")
            currMinNode = None
            currMinIdx = -1
            broken = False
            for idx, l in enumerate(lists):
                if not l:
                    lists.pop(idx)
                    broken = True
                    break
                if l.val < currMin:
                    currMinNode = l
                    currMin = l.val
                    currMinIdx = idx
            if not broken and currMinNode:
                curr.next = currMinNode
                lists[currMinIdx] = lists[currMinIdx].next
                curr = curr.next
        
        curr.next = lists[0]
        return dummy.next