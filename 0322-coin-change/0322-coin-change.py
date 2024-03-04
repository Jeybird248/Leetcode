class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        # dp[1] = 1
        for i in range(1, amount + 1):
            for coin in coins:
                if i == coin:
                    dp[i] = 1
                elif i > coin:
                    dp[i] = min(dp[i], dp[i - coin] + dp[coin])
        # print(dp)
        return dp[-1] if dp[-1] != float("inf") else -1