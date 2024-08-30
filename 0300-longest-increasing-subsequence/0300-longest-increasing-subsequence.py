class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Create an array dp where dp[i] represents the length of the longest increasing subsequence that ends with the element nums[i].
        For each nums[i], iterate through all the previous elements nums[j] where j < i.
If nums[i] > nums[j], it means you can extend the increasing subsequence that ends at nums[j] to include nums[i].
Update dp[i] as dp[i] = max(dp[i], dp[j] + 1).
"""
        maxVal = 1
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    maxVal = max(maxVal, dp[i])
                    
        return maxVal