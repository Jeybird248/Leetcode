# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = []
        count = 0
        maxNode = float('-inf')
        q.append((root, maxNode))

        while q:
            node, currMax = q.pop()
            if node.val >= currMax:
                count += 1
                currMax = node.val

            if node.left:
                q.append((node.left, currMax))
            if node.right:
                q.append((node.right, currMax))

        return count