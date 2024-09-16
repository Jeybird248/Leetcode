class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = right = 0
        maxAvg = 0
        for i in range(k):
            maxAvg += nums[right]
            right += 1
        currSum = maxAvg
        while right < len(nums):
            print(maxAvg, left, right)
            currSum = currSum - nums[left] + nums[right]
            maxAvg = max(maxAvg, currSum)
            right += 1
            left += 1
        
        return maxAvg/k
        