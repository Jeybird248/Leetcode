class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currSum = nums[0]
        for num in nums[1:]:
            if currSum <= 0:
                currSum = num
                maxSum = max(maxSum, currSum)
            else:
                currSum += num
                maxSum = max(maxSum, currSum)
        return maxSum