class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target and sorted([nums[i] , nums[j] , nums[left] , nums[right]]) not in output:
                        output.append(sorted([nums[i] , nums[j] , nums[left] , nums[right]]))
                        
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        left += 1
        return output