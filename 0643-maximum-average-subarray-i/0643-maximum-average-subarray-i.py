class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, 0
        currSum, maxSum = 0, 0
        while k:
            currSum += nums[right]
            right += 1
            k -= 1
        maxSum = currSum
        
        while right < len(nums):
            currSum += nums[right]
            currSum -= nums[left]
            maxSum = max(maxSum, currSum)
            left += 1
            right += 1
            
        return maxSum / (right - left)