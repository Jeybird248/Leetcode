# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.arr = []
        
        def dfs(root, level):
            if not root:
                return
            if level < len(self.arr):
                self.arr[level] += root.val
            else:
                self.arr.append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        return self.arr[-1]