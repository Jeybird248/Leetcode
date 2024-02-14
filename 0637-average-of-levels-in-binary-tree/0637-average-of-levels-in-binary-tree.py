# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.d = defaultdict(list)
        
        def traversal(root, level):
            if not root:
                return
            self.d[level].append(root.val)
            traversal(root.left, level + 1)
            traversal(root.right, level + 1)
        
        traversal(root, 0)
        output = []
        for level in self.d.values():
            output.append(sum(level) / len(level))
        return output