"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # a dictionary to map original nodes to their clones
        visited = {}

        def dfs(n: 'Node') -> 'Node':
            # if the node has already been cloned, return the clone
            if n in visited:
                return visited[n]
            
            # create a new clone for the current node
            clone = Node(n.val)
            visited[n] = clone

            # recursively clone all neighbors
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone

        # start dfs from the given node
        return dfs(node)