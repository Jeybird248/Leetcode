class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currSum = maxSum = 0
        for g in gain:
            currSum += g
            maxSum = max(currSum, maxSum)
        return maxSum