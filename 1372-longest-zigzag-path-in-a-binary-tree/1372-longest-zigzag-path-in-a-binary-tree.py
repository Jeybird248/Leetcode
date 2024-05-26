# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxLen = 0
        def helper(root, right, depth):
            if not root:
                return depth
            self.maxLen = max(self.maxLen, depth)
            if right:
                helper(root.right, False, depth + 1)
                helper(root.left, True, 1)
            else:
                helper(root.left, True, depth + 1)
                helper(root.right, False, 1)
        helper(root.left, True, 1)
        helper(root.right, False, 1)
        return self.maxLen