# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        maxVal = float("-inf")
        for i in range(len(arr) // 2):
            maxVal = max(arr[i] + arr[len(arr) - i - 1], maxVal)
        return maxVal