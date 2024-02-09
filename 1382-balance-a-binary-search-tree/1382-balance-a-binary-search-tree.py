# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr = []
        
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            self.arr.append(root.val)
            traversal(root.right)
            
        traversal(root)
        
        def build(left, right):
            while left <= right:
                mid = (left + right) // 2
                return TreeNode(self.arr[mid], build(left, mid - 1), build(mid + 1, right))
            return None
        left, right = 0, len(self.arr) - 1
        return build(left, right)