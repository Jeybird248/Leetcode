class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, len(nums) - 1
                
                while left < right:
                    if target == nums[i] + nums[j] + nums[left] + nums[right] and [nums[i], nums[j], nums[left] ,nums[right]] not in output:
                        output.append([nums[i], nums[j], nums[left] ,nums[right]])
                    elif target > nums[i] + nums[j] + nums[left] + nums[right]:
                        left += 1
                    else:
                        right -= 1
        return output