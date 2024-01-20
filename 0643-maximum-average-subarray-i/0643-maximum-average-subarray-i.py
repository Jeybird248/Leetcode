class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, k - 1
        s = 0
        for i in range(k):
            s += nums[i]
        maxS = s
        while right < len(nums):
            right += 1
            if right < len(nums):
                s += nums[right]
                s -= nums[left]
                maxS = s if s / k > maxS / k else maxS
                left += 1
            else:
                maxS = s if s / k > maxS / k else maxS
        return maxS / k
            