class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reds, whites, blues = 0, 0, 0
        for num in nums:
            if num == 0:
                 reds += 1
            elif num == 1:
                whites += 1
            else:
                blues += 1
        
        for idx, num in enumerate(nums):
            if reds:
                nums[idx] = 0
                reds -= 1
                continue
            if whites:
                nums[idx] = 1
                whites -= 1
                continue
            nums[idx] = 2
        