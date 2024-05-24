# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        dq = deque([root]) # deque is optimized for popping 
        num_node_level = 1 # current number of nodes left in level
        levels = 0
        while dq:
            node = dq.popleft()
            if node.left: 
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
            num_node_level -= 1
            if num_node_level == 0: # if all nodes in the level has been sold
                levels += 1 # go to next level
                num_node_level = len(dq) # count number of nodes in next level
                
        return levels