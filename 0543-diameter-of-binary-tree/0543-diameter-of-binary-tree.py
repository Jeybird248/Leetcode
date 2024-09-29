# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxLen = 0
        def recursion(root):
            if not root:
                return 0
            
            left = recursion(root.left)
            right = recursion(root.right)
            self.maxLen = max(self.maxLen, left + right)
            return max(left, right) + 1
        recursion(root)
        return self.maxLen