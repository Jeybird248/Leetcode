class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        left, right= 0, len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == middle:
                left = middle + 1
            else:
                right = middle - 1
        
        return left