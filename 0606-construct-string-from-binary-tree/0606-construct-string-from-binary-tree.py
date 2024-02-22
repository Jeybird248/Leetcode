# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.output = ""
        
        def traversal(root):
            if not root:
                return
            self.output += str(root.val)
            if root.left or root.right:
                self.output += "("
                traversal(root.left)
                self.output += ")"
            if root.right:
                self.output += "("
                traversal(root.right)
                self.output += ")"
        traversal(root)
        return self.output