class Solution:
    def allPossibleFBT(self, n: int):
        self.dp = [[] for _ in range(n + 1)]
        
        def solve(n):
            if n % 2 == 0:
                return []

            if self.dp[n]:
                return self.dp[n]

            if n == 1:
                new_node = TreeNode(0)
                return [new_node]

            res = []
            for i in range(1, n, 2):
                left = solve(i)
                right = solve(n - i - 1)

                for l in left:
                    for r in right:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)

            self.dp[n] = res
            return res
        
        return solve(n)
