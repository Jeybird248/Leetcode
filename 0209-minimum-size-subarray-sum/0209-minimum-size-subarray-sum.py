class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currSum = 0
        minLen = float("inf")
        
        for right in range(len(nums)):
            currSum += nums[right]  # add current element to the running sum

            # shrink the window from the left as long as the current sum is greater than or equal to the target
            while currSum >= target:
                minLen = min(minLen, right - left + 1)  # calculate the length of the current window
                currSum -= nums[left]  # remove the leftmost element from the sum
                left += 1  # move the left pointer to the right
        
        # if we found a valid subarray, return its length, otherwise return 0
        return minLen if minLen != float("inf") else 0