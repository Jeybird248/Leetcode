# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.arr = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.arr.append(root.val)
            inorder(root.right)
        inorder(root)
        self.arr.sort()
        root = TreeNode(self.arr.pop(0))
        curr = root
        while self.arr:
            curr.right = TreeNode(self.arr.pop(0))
            curr = curr.right
        return root