class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target not in nums:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0]
        
        def binary_search(curr_target):
            start, end = 0, len(nums) - 1
            while start <= end:
                middle = (start + end) // 2
                if nums[middle] == curr_target:
                    return middle
                elif nums[middle] < curr_target:
                    start = middle + 1
                else:
                    end = middle - 1
            return start
        
        if nums[binary_search(target)] == target:
            left, right = binary_search(target - 1), binary_search(target + 1)
            # print(left, right)
            while 0 > left or nums[left] != target:
                left += 1
            while len(nums) <= right or nums[right] != target:
                right -= 1
            return [left, right]
        return [-1, -1]