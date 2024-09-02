class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currSum = 0
        minLen = float('inf')  # Start with an infinite length to find the minimum

        # Iterate through the nums list using the right pointer
        for right in range(len(nums)):
            currSum += nums[right]  # Add the current number to the currSum
            
            # Shrink the window from the left until the currSum is less than target
            while currSum >= target:
                minLen = min(minLen, right - left + 1)  # Update the minimum length
                currSum -= nums[left]  # Subtract the leftmost element from currSum
                left += 1  # Move the left pointer to the right

        # If minLen was updated, return it; otherwise, return 0
        return minLen if minLen != float('inf') else 0