# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return  # Ensure that when the root is None, you return None

        def hasOne(node):
            if not node:
                return False
            return (node.val == 1) or (hasOne(node.left)) or (hasOne(node.right))

        if not hasOne(root):  # Corrected syntax for the 'if' condition
            del root
            return
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        return root
