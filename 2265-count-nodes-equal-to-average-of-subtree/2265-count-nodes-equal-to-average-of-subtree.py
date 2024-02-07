# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def dfs(root):
            nonlocal count
            if not root:
                return 0,0             
            ls , lc = dfs(root.left)
            rs , rc = dfs(root.right)
            if root.val == (root.val + ls + rs) // (lc + rc + 1):
                count += 1 
            return root.val + ls + rs , lc + rc + 1
        dfs(root)
        return count