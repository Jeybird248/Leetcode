# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxdiff = 0
        def traversal(root, minimum, maximum):
            if not root:
                return
            minimum = min(root.val, minimum)
            maximum = max(root.val, maximum)
            self.maxdiff = max(maximum - minimum, self.maxdiff)
            traversal(root.left, minimum, maximum)
            traversal(root.right, minimum, maximum)
            
            
        traversal(root, float("inf"), float("-inf"))
        return self.maxdiff