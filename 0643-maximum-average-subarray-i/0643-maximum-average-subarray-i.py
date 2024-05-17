class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, k - 1
        maxSum = 0
        for i in range(k):
            maxSum += nums[i]
        currSum = maxSum
        while right < len(nums) - 1:
            right += 1
            currSum = currSum - nums[left] + nums[right]
            maxSum = max(maxSum, currSum)
            left += 1
        return maxSum / k