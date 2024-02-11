"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.arr = []
        
        def traversal(root):
            if not root:
                return 
            for child in root.children:
                traversal(child)
            self.arr.append(root.val)
        traversal(root)
        return self.arr