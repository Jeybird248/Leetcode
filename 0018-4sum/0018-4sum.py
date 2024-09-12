class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array to use the two-pointer technique
        n = len(nums)
        result = []

        # First two loops to fix the first and second numbers
        for i in range(n):
            # Skip duplicate elements for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                # Skip duplicate elements for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Two-pointer approach for the remaining two numbers
                left, right = j + 1, n - 1
                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Move the left pointer past duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Move the right pointer past duplicates
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move pointers inward after finding a valid combination
                        left += 1
                        right -= 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1
        return result
