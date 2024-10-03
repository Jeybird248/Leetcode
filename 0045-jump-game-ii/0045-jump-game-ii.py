class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0
        for idx, num in enumerate(nums):
            for i in range(1, num + 1):
                if idx + i < len(nums):
                    dp[idx + i] = min(dp[idx + i], dp[idx] + 1)
                    
        return dp[-1]