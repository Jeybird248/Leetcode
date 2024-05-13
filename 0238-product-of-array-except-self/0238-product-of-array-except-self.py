class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            output[i] = product
            product *= nums[i]
        # [1, 1, 2, 6]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= product
            product *= nums[i]
        return output
        # [24, 12, 8, 6]