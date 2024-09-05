# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxPath = 0
        
        def recursion(root):
            if not root:
                return
            self.maxPath = max(self.maxPath, height(root.left) + height(root.right))
            recursion(root.left)
            recursion(root.right)
            
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
            
        
        recursion(root)
        return self.maxPath
    