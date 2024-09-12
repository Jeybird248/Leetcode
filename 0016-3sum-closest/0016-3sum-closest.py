class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestDiff = float("inf")
        nums.sort()
        n= len(nums)
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if target - curr_sum == 0:
                    return target
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
                closestDiff = curr_sum if abs(target - closestDiff) > abs(target - curr_sum) else closestDiff
        
        return closestDiff