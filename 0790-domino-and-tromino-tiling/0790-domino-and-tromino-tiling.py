class Solution:
    def numTilings(self, n: int) -> int:
        # 0 = 0
        # 1 = 1
        # 2 = 1 * 2 + 0 = 2
        # 3 = 2 * 2 + 1 = 5
        # 4 = 5 * 2 + 1 = 11
        # 5 = 11 * 2 + 2 =  24
        # 6 = 24 * 2 + 5 = 53
        # 7 = 53 * 2 + 11 = 117
        dp = [0] * (n + 5)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        dp[4] = 11
        for i in range(5, n + 1):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % (10**9 + 7)
        return dp[n]