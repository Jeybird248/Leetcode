class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, 0
        maxSum = 0
        while right < k:
            maxSum += nums[right]
            right += 1
        currSum = maxSum
        while right < len(nums):
            currSum = currSum + nums[right] - nums[left]
            maxSum = max(maxSum, currSum)
            left += 1
            right += 1
            
        return maxSum / k