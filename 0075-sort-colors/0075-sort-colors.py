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
            elif num == 2:
                blues += 1
        
        pointer = 0
        while reds:
            nums[pointer] = 0
            pointer += 1
            reds -= 1
        while whites:
            nums[pointer] = 1
            pointer += 1
            whites -= 1
        while blues:
            nums[pointer] = 2
            pointer += 1
            blues -= 1
        
        