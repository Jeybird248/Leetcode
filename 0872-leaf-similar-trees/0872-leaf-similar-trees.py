# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr1 = []
        self.arr2 = []
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traversal(root, arr):
            if not root:
                return
            if not root.left and not root.right:
                arr.append(root.val)
            traversal(root.left, arr)
            traversal(root.right, arr)
            
        traversal(root1, self.arr1)
        traversal(root2, self.arr2)
        return self.arr1 == self.arr2