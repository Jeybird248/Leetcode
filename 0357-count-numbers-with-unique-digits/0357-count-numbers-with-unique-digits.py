

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
        n = min(n, 8)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 10
        for i in range(2, n + 1):
            choices = 9
            for j in range(i - 1):
                choices *= 9 - j
            dp[i] = dp[i - 1] + choices
        return dp[-1]