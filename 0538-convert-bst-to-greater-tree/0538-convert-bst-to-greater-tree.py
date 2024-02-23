# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        def traversal(root):
            if not root:
                return
            traversal(root.right)
            root.val, self.total = self.total + root.val, self.total + root.val
            traversal(root.left)
        traversal(root)
        return root