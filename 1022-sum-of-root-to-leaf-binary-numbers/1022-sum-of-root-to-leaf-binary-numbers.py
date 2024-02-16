# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.output = 0
        def traversal(root, string):
            if not root:
                return
            string += str(root.val)
            if not root.left and not root.right:
                self.output += int(string, 2)
            traversal(root.left, string)
            traversal(root.right, string)
        traversal(root, "")
        return self.output