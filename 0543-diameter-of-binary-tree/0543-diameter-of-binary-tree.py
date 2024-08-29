# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0
        
        def recursion(node):
            if not node:
                return 0
            
            left_height = recursion(node.left)
            right_height = recursion(node.right)
            
            # Update the maximum diameter at this node
            self.maximum = max(self.maximum, left_height + right_height)
            
            # Return the height of the current node
            return max(left_height, right_height) + 1
        
        recursion(root)
        return self.maximum
            
            