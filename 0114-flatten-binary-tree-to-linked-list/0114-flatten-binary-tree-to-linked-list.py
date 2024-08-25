# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        def traversal(root):
            if not root:
                return
            stack.append(root)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        curr = root
        for node in stack[1:]:
            curr.left = None
            curr.right = node
            curr = curr.right
        