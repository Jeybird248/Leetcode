"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.output = defaultdict(list)
        def traversal(root, level):
            if not root:
                return
            self.output[level].append(root.val)
            for child in root.children:
                traversal(child, level + 1)
        traversal(root, 0)
        return list(self.output.values())
            