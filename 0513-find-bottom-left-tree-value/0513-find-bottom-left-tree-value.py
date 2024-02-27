# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.value = root.val
        self.depth = 0
        
        def traversal(root, depth):
            if not root:
                return
            traversal(root.left, depth + 1)
            if depth > self.depth:
                self.value = root.val
                self.depth = depth
            traversal(root.right, depth + 1)
        traversal(root, 0)
        return self.value
        
        