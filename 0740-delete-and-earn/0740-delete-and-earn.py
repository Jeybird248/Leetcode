class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        m = max(nums)
        points = [0] * (m + 1)
        
        for num in nums:
            points[num] += num
        
        prev = curr = 0
        for i in range(len(points)):
            prev, curr = curr, max(prev + points[i], curr)
        
        return curr