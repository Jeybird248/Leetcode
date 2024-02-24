# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def traversal(root, counts):
            if not root:
                return
            
            counts[root.val] += 1
            
            if not root.left and not root.right:
                oddCount = sum(count % 2 == 1 for count in counts.values())
                self.count += 1 if oddCount <= 1 else 0
            else:
                traversal(root.left, counts.copy()) 
                traversal(root.right, counts.copy())
        
        traversal(root, defaultdict(int))
        return self.count