from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0  # This will track the sum of the current window
        min_len = float("inf")  # Use to find the minimum length
        
        for right in range(len(nums)):
            current_sum += nums[right]  # Expand the window by moving the right pointer
            
            # Contract the window until the sum is less than the target
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)  # Update minimum length
                current_sum -= nums[left]  # Shrink the window by moving the left pointer
                left += 1
        
        return min_len if min_len != float("inf") else 0
