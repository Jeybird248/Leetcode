class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = right = 0
        currSum = maxSum = 0
        for i in range(k):
            currSum += nums[right]
            right += 1
        maxSum = currSum
        while right < len(nums):
            currSum = currSum - nums[left] + nums[right]
            maxSum = max(maxSum, currSum)
            left += 1
            right += 1
        return maxSum / k