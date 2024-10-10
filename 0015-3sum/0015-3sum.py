class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()  # use a set to store unique triplets
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates for `i`
                continue
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Add the triplet as a tuple to avoid duplicates and re-sorting
                    output.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for `left` and `right`
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1
        
        # Convert the set of tuples back to a list of lists for the final output
        return [list(triplet) for triplet in output]
