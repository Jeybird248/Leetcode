class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(nums[i] + 1):
                if i + j < len(dp):
                    dp[i + j] = min(dp[i] + 1, dp[i + j])        
        return dp[-1]