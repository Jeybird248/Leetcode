class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = n - 2

        # Step 1: Find the first decreasing element from the end
        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1

        # Step 2: If we found a valid left index
        if left >= 0:
            right = n - 1
            # Find the smallest number larger than nums[left]
            while nums[right] <= nums[left]:
                right -= 1
            # Swap them
            nums[left], nums[right] = nums[right], nums[left]
        
        # Step 3: Reverse the subarray to the right of left (or the whole array if no valid left)
        left += 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
