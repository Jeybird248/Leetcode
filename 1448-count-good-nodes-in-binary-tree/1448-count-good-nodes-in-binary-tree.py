class Solution:
    def helper(self, root, max_val):
        if not root:
            return
        if root.val >= max_val:
            self.count += 1
            max_val = root.val
        self.helper(root.left, max_val)
        self.helper(root.right, max_val)

    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.helper(root, root.val)
        return self.count