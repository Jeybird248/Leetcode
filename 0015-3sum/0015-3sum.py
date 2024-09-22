class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort the array first
        output = []
        
        for i in range(len(nums) - 2):  # iterate up to len(nums) - 2
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates for `i`
                continue
            
            left, right = i + 1, len(nums) - 1  # two pointers
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # skip duplicates for left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return output