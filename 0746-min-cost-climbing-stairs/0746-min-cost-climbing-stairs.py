class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost))
        n = len(dp)
        for i in range(n - 1, -1, -1):
            first = dp[i+1] if i + 1 < n else 0
            second = dp[i+2] if i + 2 < n else 0
            dp[i] = cost[i] + min(first, second)
        return min(dp[0], dp[1])
        