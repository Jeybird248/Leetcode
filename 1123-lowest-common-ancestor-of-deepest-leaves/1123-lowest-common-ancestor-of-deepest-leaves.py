# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.output = None
        self.max_depth = -1

        def traversal(root, depth):
            if not root:
                return depth

            left = traversal(root.left, depth + 1)
            right = traversal(root.right, depth + 1)

            # Update output when both left and right subtrees have the maximum depth
            if left == right and left >= self.max_depth:
                self.max_depth = left
                self.output = root

            return max(left, right)

        traversal(root, 0)
        return self.output
