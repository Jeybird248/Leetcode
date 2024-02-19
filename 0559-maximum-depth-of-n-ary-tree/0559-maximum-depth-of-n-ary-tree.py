"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def depth(node, level):
            if not node:
                return level - 1
            return max([depth(child, level + 1) for child in node.children] + [level])

        return depth(root, 1)