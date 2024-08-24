# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        self.max_level = -1
        def traversal(root, level):
            if not root:
                return
            if level > self.max_level:
                output.append([root.val])
                self.max_level = level
            else:
                output[level].append(root.val)
            traversal(root.left, level + 1)
            traversal(root.right, level + 1)
            
        traversal(root, 0)
        return output