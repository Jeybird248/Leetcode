# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxLen = 0            
        def dfs(root, currLen, right):
            if not root:
                return currLen
            self.maxLen = max(self.maxLen, currLen)
            if right:
                dfs(root.left, 1, True)
                dfs(root.right, currLen + 1, False)
            else:
                dfs(root.left, currLen + 1, True)
                dfs(root.right, 1, False)
            
        if root.left:
            leftCount = dfs(root.left, 1, True)
        if root.right:
            rightCount = dfs(root.right, 1, False)
        return self.maxLen