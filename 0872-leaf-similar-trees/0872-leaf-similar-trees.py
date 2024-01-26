# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(root, stack):
            if not root:
                return None
            helper(root.left, stack)
            if not root.left and not root.right:
                stack.append(root.val)
            helper(root.right, stack)
        helper(root1, self.stack1)
        helper(root2, self.stack2)
        return self.stack1 == self.stack2