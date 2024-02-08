# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.evenGrandParent = []
        
        def dfs(node, parent=None, grandParent=None):
            if node is None:
                return
            # print(node.val, parent, grandParent)

            if grandParent and grandParent % 2 == 0:
                self.evenGrandParent.append(node.val)
            
            dfs(node.right, node.val, parent)
            dfs(node.left, node.val, parent)
        
        
        dfs(root)
        
        return sum(self.evenGrandParent)