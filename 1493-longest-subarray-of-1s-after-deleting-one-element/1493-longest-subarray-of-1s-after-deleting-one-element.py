class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = 0
        K = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                K -= 1        
            if K < 0:
                if nums[left] == 0:
                    K += 1
                left += 1
        return right - left