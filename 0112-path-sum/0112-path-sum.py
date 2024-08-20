# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse(root, targetSum2):
            if not root:
                return False
            if not root.left and not root.right:
                return targetSum2 == root.val
            check1 = False
            check2 = False
            if root.left:
                check1 = traverse(root.left, targetSum2 - root.val)
            if root.right:
                check2 =  traverse(root.right, targetSum2 - root.val)
            return check1 or check2
        
        return traverse(root, targetSum)