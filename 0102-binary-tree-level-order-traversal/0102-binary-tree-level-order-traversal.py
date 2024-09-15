# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        
        def traversal(root, height):
            if not root:
                return
            if len(output) <= height:
                output.append([root.val])
            else:
                output[height].append(root.val)
            traversal(root.left, height + 1)
            traversal(root.right, height + 1)
        
        traversal(root, 0)
        return output