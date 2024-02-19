# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr=[]
        
        def traversal(root):
            if not root or len(self.arr) >= k:
                return
            traversal(root.left)
            self.arr.append(root.val)
            traversal(root.right)
        
        traversal(root)
        return self.arr[k - 1]