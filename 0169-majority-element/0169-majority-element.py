class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        max_count_element = nums[0]
        if len(nums) == 1:
            return nums[0]
        for num in nums[1:]:
            if num == max_count_element:
                counter += 1
            else:
                counter -= 1
            if not counter:
                counter = 1
                max_count_element = num
        return max_count_element
                