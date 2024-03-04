class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        
        # Iterate from 2 to n
        for i in range(2, n + 1):
            # Iterate from 1 to i - 1
            for j in range(1, i):
                # Calculate the maximum product
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        # print(dp)
        # Return the maximum product
        return dp[n]