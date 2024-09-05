class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currSum = nums[0]
        
        for num in nums[1:]:
            currSum = max(num, currSum + num)  # update current sum: either extend or start fresh
            maxSum = max(maxSum, currSum)  # update max sum if current sum is higher
        
        return maxSum