class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_length = 0 
        for num in arr:
            length = dp.get(num - difference, 0) + 1
            dp[num] = length  
            max_length = max(max_length, length) 
            
        return max_length